# management/admin.py
from django.contrib import admin
from .models import GalleryImage, ManagementProfile

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_by', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(ManagementProfile)
class ManagementProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)