# management/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class GalleryImage(models.Model):
    SECTION_CHOICES = [
        ('first', 'First Section'),
        ('second', 'Second Section'),
        ('third', 'Third Section'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES, default='first')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']  # <-- Oldest first, newest last

    def __str__(self):
        return self.title

class Career(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=100)
    duties = models.TextField()   # Will store bullet points separated by new lines
    apply_note = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_duties_list(self):
        return self.duties.split("\n")  # convert textarea into list

    def __str__(self):
        return self.title
    
class ManagementProfile(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    profile_pic = models.ImageField(upload_to='management_pics/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name
