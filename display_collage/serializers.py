from rest_framework import serializers
from .models import Album, Collage

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album 
        fields = ('cover_art_img')

class CollageSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Collage
        # fields = ['img', 'img_url']
        fields = ['img', 'img_url', 'img_str']

    
    def get_img_url(self, collage):
        request = self.context.get('request')
        img_url = collage.img.url
        return request.build_absolute_uri(img_url)