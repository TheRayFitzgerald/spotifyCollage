from importlib.metadata import metadata
from unicodedata import name
from django.shortcuts import render
import spotipy

from .models import Album, Collage, User
from .serializers import *
from django.shortcuts import render
from django.views import generic

from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from math import isqrt
from concurrent import futures
import queue
from django.core.files.base import ContentFile
import logging, base64

log = logging.getLogger(__name__)


NUMBER_OF_ALBUMS = 50
PERIOD = "long_term"
IMAGE_QUALITY = 1

imgdict = dict()
q = queue.Queue()


@api_view(['GET'])
def albums_list(request):

    log.warning('Starting API')

    # get the spotify album data
    try:
        albums_set, user = get_spotify_album_data(request)
    except Exception as e:
        log.error("get_spotify_album_data failed: %s" % e)
    
    # download the album cover art images
    img_list = download_imgs(albums_set)

    # generate the collage using the images
    collage_img = generate_collage(img_list)
    
    # create the collage object 
    collage =  save_collage(collage_img, user)

    # serialize the collage object
    serializer = CollageSerializer(collage, context={'request': request})
    return Response(serializer.data)


def get_spotify_album_data(request):

    Album.objects.all().delete()
    albums_set = set()

    token = request.GET.get('token')
    
    spotify = spotipy.Spotify(token)

    # Create user object 
    current_user = spotify.current_user()
    user, created = User.objects.get_or_create(display_name=current_user['display_name'], metadata=current_user)

    # results1 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='short_term')
    # results2 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range='medium_term')
    results3 = spotify.current_user_top_tracks(limit=NUMBER_OF_ALBUMS, time_range=PERIOD)
    
    for track in results3['items']:
        album = Album(title=track['album']['name'], cover_art_url=track['album']['images'][IMAGE_QUALITY]['url'])
        albums_set.add(album)

    return albums_set, user


def generate_collage(img_list):

    img_rows = list()
    n_rows = isqrt(len(img_list))
    # print('len img_list: %i' % len(img_list))
    # print('n_rows: %i' % n_rows)

    for i in range(0, n_rows):
        try:
            img_row = Image.fromarray(
                
                    np.concatenate(
                        [np.array(x.resize((300,300))) for x in img_list[(i * n_rows):(i * n_rows + n_rows)]],
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

def save_collage(collage_img, user):

    # Buffer
    collage_image_io = BytesIO()
    collage_img.save(collage_image_io, format='jpeg')
    
    ## Old filecontent image saving
    
    # img_content = ContentFile(collage_image_io.getvalue())
    # collage.img.save("collage.jpg", img_content, save=False)


    # base64 encoded image (string)
    
    img_str = base64.b64encode(collage_image_io.getvalue()).decode('ascii')
    # log.warning("img_str field: %s" % img_str)
    
    collage = Collage(user=user, img_str=img_str)
    
    collage.save()

    return collage

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


