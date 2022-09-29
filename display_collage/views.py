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

NUMBER_OF_ALBUMS = 50
PERIOD = "short_term"



@api_view(['GET'])
def albums_list(request):

        Album.objects.all().delete()
        albums_set = set()

        print('getting token from url')
        token = request.GET.get('token')
        print(token)

        #social = self.request.user.social_auth.get(provider='spotify')
        # print('social' + social.extra_data + 'socialend')
        

        # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='30a5904c955c4c92b9543e2f9bfb05c7', client_secret='885d1d474fe4434688e8ff5049ff8df3'))
        spotify = spotipy.Spotify(token)

        results1 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='short_term')
        results2 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='medium_term')
        results3 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='long_term')
        # print('results')
        # print(len(results1))
        # print(results1)
        for track in results1['items']:
            print('results1')
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][0]['url'])
            album.save()
            albums_set.add(album)

        for track in results2['items']:
            print('results2')
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][0]['url'])
            album.save()
            albums_set.add(album)
        
        for track in results3['items']:
            print('results2')
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][0]['url'])
            album.save()
            albums_set.add(album)




        data = Album.objects.all()
        print("N ALBUMS")
        print(len(data))
        
        serializer = AlbumSerializer(albums_set, context={'request': request}, many=True)

        return Response(serializer.data)

