# book/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

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
    title = models.CharField(max_length=255)  # Title of the book/file
    description = models.TextField(blank=True, null=True)  # Description of the book/file
    visibility = models.BooleanField(default=True)  # Visibility status (public/private)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Cost of the file
    year_published = models.IntegerField(blank=True, null=True)  # Year of publication
    file = models.FileField(upload_to='uploads/')  # The uploaded file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the upload

    def __str__(self):
        return self.title  # You can modify this to return the title or any field you prefer
    
