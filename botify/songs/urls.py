from django.urls import path
from songs import views
from django.views.generic import TemplateView

urlpatterns = [
    path('songs/<int:pk>/', views.SongDetail, name='detail'),
    path('songs/<int:song_id>/like/', views.LikeSong, name='like'),
    path('upload/', views.SongUpload, name='upload'),
    path('songs/choose/thumbnail/<int:pk>/', views.choose_thumbnail, name='choose_thumbnail'),
    path('songs/set/thumbnail/<int:song_id>/<int:thumbnail_id>/', views.set_thumbnail, name='set_thumbnail'),
]