from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .models import Album
from .serializers import *
from django.shortcuts import render
from django.views import generic

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



class IndexView(generic.ListView):

    template_name = 'display_collage/index.html'
    context_object_name = 'album_list'


    def get_queryset(self):
        """Return the last five published ideas."""

        Album.objects.all().delete()

        print('getting code')
        code = self.request.GET.get('code')
        print(code)


        
        social = self.request.user.social_auth.get(provider='spotify')
        
        print('social')
        print(social.extra_data)
        print('socialend')
        

        # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='30a5904c955c4c92b9543e2f9bfb05c7', client_secret='885d1d474fe4434688e8ff5049ff8df3'))
        spotify = spotipy.Spotify(social.extra_data['access_token'])

        results = spotify.current_user_top_tracks(limit=10)
        print('results')
        print(results)
        for track in results['items'][:10]:
            print('track    : ' + track['name'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][0]['url'])
            album.save()
            

        data = Album.objects.all()
        return data
        '''
        serializer = AlbumSerializer(data, context={'request': self.request}, many=True)

        return Response(serializer.data)
        '''

@api_view(['GET'])
def albums_list(request):

        Album.objects.all().delete()

        print('getting code')
        code = request.GET.get('code')
        print(code)


        
        social = request.user.social_auth.get(provider='spotify')
        
        print('social')
        print(social.extra_data)
        print('socialend')
        

        # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='30a5904c955c4c92b9543e2f9bfb05c7', client_secret='885d1d474fe4434688e8ff5049ff8df3'))
        spotify = spotipy.Spotify(social.extra_data['access_token'])

        results = spotify.current_user_top_tracks(limit=10)
        print('results')
        print(results)
        for track in results['items'][:10]:
            print('track    : ' + track['name'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][0]['url'])
            album.save()
            

        data = Album.objects.all()
        
        serializer = AlbumSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

