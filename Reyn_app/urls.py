from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.contact_submit, name='contact_submit'),
]