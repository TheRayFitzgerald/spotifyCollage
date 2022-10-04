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
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from math import isqrt



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

        # results1 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='short_term')
        # results2 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='medium_term')
        results3 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='long_term')
        # print('results')
        # print(len(results1))
        # print(results1)
        '''
        for track in results1['items']:
            print('results1')
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][2]['url'])
            album.save()
            albums_set.add(album)

        for track in results2['items']:
            print('results2')
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['name'], cover_art_url=track['album']['images'][2]['url'])
            album.save()
            albums_set.add(album)
        '''
        for track in results3['items']:
            # print('track    : ' + track['name'])
            # print('cover art: ' + track['album']['images'][0]['url'])
            # print()

            album = Album(title=track['album']['name'], cover_art_url=track['album']['images'][2]['url'])
            album.save()
            albums_set.add(album)



        data = Album.objects.all()
        
        '''
        filenames=list()
        for i, album in enumerate(data):
            img_data = requests.get(album.cover_art_url).content
            filename = 'image_%s.jpg' % i
            with open('./images/%s' % filename, 'wb') as handler:
                handler.write(img_data)
            
            filenames.append(filename)
        '''
        
        img_list = download_images(albums_set)
        collage_img = generate_collage(img_list)
        collage_img.save('./collage_img.jpg')
        

        print("N ALBUMS")
        print(len(data))
        
        serializer = AlbumSerializer(albums_set, context={'request': request}, many=True)

        return Response(serializer.data)

def generate_collage(img_list):

    img_rows = list()
    n_rows = isqrt(len(img_list))
    print('len img_list: %i' % len(img_list))
    print('n_rows: %i' % len(n_rows))

    for i in range(0, n_rows):
        try:
            img_row = Image.fromarray(
                
                    np.concatenate(
                        [np.array(x.resize((64,64))) for x in img_list[(i * n_rows):(i * n_rows + n_rows)]],
                        axis=1
                    )
            )
        except Exception as e:
            print('ray, exception %s' % str(e))
            print(img_list[(i * n_rows):(i * n_rows + n_rows)])
        img_rows.append(img_row)
    
    concatenated = Image.fromarray(
            np.concatenate(
                [np.array(x) for x in img_rows],
                axis=0
            )
        )

    return concatenated


def download_images(album_list):

    img_list = list()
    for i, album in enumerate(album_list):
        print('downloading %s' % i)
        response = requests.get(album.cover_art_url)
        img = Image.open(BytesIO(response.content))
        img_list.append(img)
    
    return img_list