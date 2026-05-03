from django.contrib import admin
from .models import Subject, Material

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'description']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
  list_display = ['id', 'subject', 'title', 'file', 'created_at', 'currentUser']