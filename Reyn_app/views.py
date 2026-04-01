from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import (
    Home, About, Skill, Project, Education, SocialLink, ContactMessage
)

def home(request):
    # Get home data
    home_data = Home.objects.first()
    
    # Get about data
    about_data = About.objects.first()
    
    # Get all skills and organize them by category
    all_skills = Skill.objects.all().order_by('category', 'order')
    
    # Organize skills by category for easier access in template
    skills_by_category = {
        'frontend': [],
        'backend': [],
        'tools': [],
    }
    
    for skill in all_skills:
        if skill.category == 'frontend':
            skills_by_category['frontend'].append(skill)
        elif skill.category == 'backend':
            skills_by_category['backend'].append(skill)
        elif skill.category == 'tools':
            skills_by_category['tools'].append(skill)
    
    # Get projects
    projects = Project.objects.filter(is_active=True).order_by('order')
    
    # Get education
    education = Education.objects.all().order_by('order')
    
    # Get social links
    social_links = SocialLink.objects.all().order_by('order')
    
    context = {
        'home': home_data,
        'about': about_data,
        'skills': all_skills,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'education': education,
        'social_links': social_links,
    }
    
    return render(request, 'Reyn_app/indexh.html', context)

@csrf_exempt
def contact_submit(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject', '')
            message = data.get('message')
            
            # Save to database
            contact = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send email notification (optional)
            if settings.EMAIL_HOST_USER:
                send_mail(
                    f'Portfolio Contact: {subject or "No Subject"}',
                    f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)