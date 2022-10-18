from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    re_path(r'^api/albums/$', views.albums_list),
    re_path(r'^api/collages/$', views.collage_list),
    path('display_collage/', views.albums_list),    
]