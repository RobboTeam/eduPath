from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
  name = models.CharField(null=False, max_length=50)
  description = models.TextField(null=False, max_length=225)
  
  def __str__(self):
    return self.name

class Material(models.Model):
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="materials")
  title = models.CharField(null=False, max_length=50) 
  file = models.FileField(null=False, upload_to='static/')
  created_at = models.DateTimeField(auto_now_add=True)
  currentUser = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} ({self.subject.name})"