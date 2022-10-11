from unicodedata import name
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
from concurrent import futures
import queue
from django.core.files.base import ContentFile



NUMBER_OF_ALBUMS = 50
PERIOD = "long_term"

imgdict = dict()
q = queue.Queue()



@api_view(['GET'])
def albums_list(request):

        albums_set = get_spotify_album_data(request)
        
        img_list = download_imgs(albums_set)
        collage_img = generate_collage(img_list)
        # collage_img.save('./collage_img.jpg')

        collage_image_io = BytesIO()
        collage_img.save(collage_image_io, format='jpeg')
        img_content = ContentFile(collage_image_io.getvalue())
        
        collage = Collage()
        collage.img.save("collage.jpg", img_content, save=False)
        collage.save()

        # collage.save("test_name", ContentFile(collage_image_io.getvalue()))
        # Collage.objects.create(name="test_name", img=ContentFile(collage_image_io.getvalue()))

        # print('saved collage img url')
        # print(collage.img)       
        # print(collage)
        # print(collage_image_io.getvalue())
        # collage_album = Album(cover_art_img=collage_img)
        
        # serializer = AlbumSerializer(collage_album, context={'request': request}, many=True)
        serializer = CollageSerializer(collage, context={'request': request})
        collage_img.save('./collage_img9.jpg')
        return Response(serializer.data)


def get_spotify_album_data(request):

    Album.objects.all().delete()
    albums_set = set()

    token = request.GET.get('token')
    

    #social = self.request.user.social_auth.get(provider='spotify')
    # print('social' + social.extra_data + 'socialend')
    

    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='30a5904c955c4c92b9543e2f9bfb05c7', client_secret='885d1d474fe4434688e8ff5049ff8df3'))
    spotify = spotipy.Spotify(token)

    # results1 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='short_term')
    # results2 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='medium_term')
    results3 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range=PERIOD)
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
        albums_set.add(album)

    return albums_set



def generate_collage(img_list):

    img_rows = list()
    n_rows = isqrt(len(img_list))
    # print('len img_list: %i' % len(img_list))
    # print('n_rows: %i' % n_rows)

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

def download_imgs(album_list):

    img_list = list()

    # download 8 at a time
    with futures.ThreadPoolExecutor(8) as executor:
        future_url = {executor.submit(download_img, album): album for album in album_list}
        for future in futures.as_completed(future_url):
            try:
                img = future.result()
                img_list.append(img)
            except Exception as e:
                print('Looks like something went wrong:', e)

    return img_list

def download_img(album):

    response = requests.get(album.cover_art_url)
    img = Image.open(BytesIO(response.content))
    if img.mode != 'RGB':
        # print('Converting to RGB: %s' % img.mode)
        img = img.convert('RGB')
    
    return img
        
@api_view(['GET'])
def collage_list(request):


        # serializer = CollageSerializer(Collage.objects.all(), context={'request': request})
        serializer = CollageSerializer(Collage.objects.all(), context={'request': request}, many=True)
        print('Collage data')
        print(serializer.data)
        return Response(serializer.data)
