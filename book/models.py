# book/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    @property
    def age(self):
        if self.birth_year:
            return date.today().year - self.birth_year
        return None

    def __str__(self):
        return self.username


class UploadedFile(models.Model):
    user = models.ForeignKey(
        
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,  # Delete files if the user is deleted
        related_name='uploaded_files'  # Optional: for reverse relations
        
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title