from django.urls import path
from . import views
from .views import project_list_api

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('youtube/', views.youtube, name='youtube'),
    path('ai-lab/', views.ai_lab, name='ai_lab'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('work-approach/', views.work_approach, name='work_approach'),
    path('ai-demo/', views.ai_demo, name='ai_demo'),
     path('api/projects/', project_list_api, name='api-projects'),
]


