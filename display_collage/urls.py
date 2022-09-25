from django.urls import path
from . import views

urlpatterns = [
    path('display_collage', views.index, name='index'),
]