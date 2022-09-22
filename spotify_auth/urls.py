from django.urls import path

from . import views


app_name = 'spotify_auth'
urlpatterns = [
    path('', views.login, name='login'),
]

