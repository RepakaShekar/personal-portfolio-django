
# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    BADGE_CHOICES = [
        ('popular', 'Popular'),
        ('premium', 'Premium'),
        ('new', 'New'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=100)
    features = models.TextField(help_text="Comma separated features")
    badge = models.CharField(
        max_length=20,
        choices=BADGE_CHOICES,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AIFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150, help_text="Client / Recruiter / Mentor")
    feedback = models.TextField()
    rating = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
    
class WorkApproach(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        help_text="Font Awesome icon class (e.g. fa-code, fa-comments)"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



