
# Create your views here.
from django.shortcuts import render
from .models import Project, Service, YouTubeVideo, AIFeature, Resume, WorkApproach, Blog
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def skills(request):
    return render(request, 'core/skills.html')

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/projects.html', {'projects': projects})

def services(request):
    services = Service.objects.filter(is_active=True)

    for service in services:
        service.feature_list = service.features.split(',')

    return render(request, 'core/services.html', {'services': services})

def youtube(request):
    videos = YouTubeVideo.objects.filter(is_active=True).order_by('-published_date')
    return render(request, 'core/youtube.html', {'videos': videos})

def ai_lab(request):
    features = AIFeature.objects.filter(is_active=True)
    return render(request, 'core/ai_lab.html', {'features': features})


def ai_demo(request):
    suggestion = None

    if request.method == 'POST':
        situation = request.POST.get('situation')
        suggestion = f"For your situation '{situation}', I recommend prioritizing one task and executing it step by step."

    return render(request, 'core/ai_demo.html', {'suggestion': suggestion})


def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'success': success
    })

def resume(request):
    resume = Resume.objects.last()
    return render(request, 'core/resume.html', {'resume': resume})

def work_approach(request):
    approaches = WorkApproach.objects.filter(is_active=True)
    return render(request, 'core/work_approach.html', {
        'approaches': approaches
    })


def blog(request):
    posts = Blog.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'core/blog.html', {'posts': posts})


def ai_demo(request):
    suggestion = None

    if request.method == 'POST':
        situation = request.POST.get('situation', '').lower()

        if 'freelance' in situation:
            suggestion = "Focus on delivering the freelance task first. Revenue-generating work should be prioritized."
        elif 'learn' in situation:
            suggestion = "Schedule focused learning blocks and avoid context switching."
        elif 'youtube' in situation:
            suggestion = "Batch content creation to stay consistent without burnout."
        else:
            suggestion = "Break your task into smaller steps and complete one at a time."

    return render(request, 'core/ai_demo.html', {'suggestion': suggestion})




