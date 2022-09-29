import datetime

from django.db import models
from django.utils import timezone


class Album(models.Model):
    title = models.CharField(primary_key=True, max_length=500)
    cover_art_url = models.URLField(max_length=200)


    def __str__(self):
        return self.title

