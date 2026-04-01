from django.contrib import admin
from .models import (
    Home, About, Goal, Statistic, Skill, Project, 
    ProjectTag, Education, SocialLink, ContactMessage
)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'availability']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'surname', 'photo')
        }),
        ('Content', {
            'fields': ('tagline', 'availability')
        }),
    )

class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1
    fields = ['goal_text', 'order']

class StatisticInline(admin.TabularInline):
    model = Statistic
    extra = 1
    fields = ['number', 'label', 'order']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description_1', 'description_2', 'description_3')
        }),
    )
    inlines = [GoalInline, StatisticInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage', 'order']
    list_filter = ['category']
    list_editable = ['percentage', 'order']
    search_fields = ['name']

class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 2
    fields = ['tag_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_number', 'is_active', 'order']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'project_number', 'order', 'is_active')
        }),
        ('Images & Links', {
            'fields': ('image_placeholder', 'github_url', 'live_url')
        }),
    )
    inlines = [ProjectTagInline]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'year', 'order']
    list_editable = ['order']
    search_fields = ['degree', 'school']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order']
    list_editable = ['order']
    search_fields = ['name']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    
    def has_add_permission(self, request):
        return False