from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album 
        fields = ('pk', 'title', 'cover_art_url')