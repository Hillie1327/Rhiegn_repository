from django.db import models
from django.utils import timezone

class Home(models.Model):
    """Home section content"""
    name = models.CharField(max_length=100, default='Alex')
    surname = models.CharField(max_length=100, default='Rivera')
    tagline = models.TextField(default='Full-Stack Developer crafting thoughtful digital experiences from pixels to databases.')
    availability = models.CharField(max_length=100, default='Available for Work')
    photo = models.ImageField(upload_to='portfolio/photos/', blank=True, null=True)
    
    def __str__(self):
        return f"Home - {self.name} {self.surname}"
    
    class Meta:
        verbose_name_plural = "Home Content"

class About(models.Model):
    """About section content"""
    title = models.CharField(max_length=200, default='A Little About Myself')
    description_1 = models.TextField()
    description_2 = models.TextField(blank=True)
    description_3 = models.TextField(blank=True)
    
    def __str__(self):
        return "About Content"
    
    class Meta:
        verbose_name_plural = "About Content"

class Goal(models.Model):
    """Career goals"""
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='goals')
    goal_text = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.goal_text[:50]

class Statistic(models.Model):
    """Statistics like years of experience, projects completed"""
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='statistics')
    number = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Statistics"
    
    def __str__(self):
        return f"{self.number} - {self.label}"

class Skill(models.Model):
    """Skills with percentages"""
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools & Cloud'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.IntegerField(help_text="Percentage from 0-100")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class Project(models.Model):
    """Projects section"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_placeholder = models.ImageField(upload_to='portfolio/photos/', blank=True, null=True)
    project_number = models.IntegerField(help_text="Display order number")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class ProjectTag(models.Model):
    """Tags for projects"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    tag_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tag_name

class Education(models.Model):
    """Education timeline"""
    year = models.CharField(max_length=100, help_text="e.g., 2020 – 2024")
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.school}"

class SocialLink(models.Model):
    """Social media links"""
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=10, help_text="Emoji or short text for icon")
    url = models.URLField()
    email = models.EmailField(blank=True, help_text="If this is email link")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at}"