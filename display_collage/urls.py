from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/albums/$', views.albums_list),
    path('display_collage/', views.albums_list),    
]