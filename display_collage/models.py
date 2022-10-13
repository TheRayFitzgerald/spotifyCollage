import datetime

from django.db import models
from django.utils import timezone



class User(models.Model):
    display_name = models.CharField(default="empty display name", primary_key=True, max_length=500)
    metadata = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharField(primary_key=True, max_length=500)
    cover_art_url = models.URLField(max_length=200)
    cover_art_img = models.ImageField(default=None, null=True)

    def __str__(self):
        return self.title

class Collage(models.Model):
    img = models.ImageField(default=None, upload_to='media/', null=False)

    # Link many-to-one (collages -> user)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







