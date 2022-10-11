import datetime

from django.db import models
from django.utils import timezone


class Album(models.Model):
    title = models.CharField(primary_key=True, max_length=500)
    cover_art_url = models.URLField(max_length=200)
    cover_art_img = models.ImageField(default=None, null=True)

    def __str__(self):
        return self.title


class Collage(models.Model):
    img = models.ImageField(default=None, upload_to='media/', null=False)
    # img_url = models.TextField(default=img.url)




