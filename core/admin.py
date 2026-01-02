from django.contrib import admin

# Register your models here.

from .models import Project, Service, YouTubeVideo, AIFeature, ContactMessage, Resume, Testimonial, WorkApproach, Blog

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(YouTubeVideo)
admin.site.register(AIFeature)
admin.site.register(ContactMessage)
admin.site.register(Resume)
admin.site.register(Testimonial)
admin.site.register(WorkApproach)
admin.site.register(Blog)




