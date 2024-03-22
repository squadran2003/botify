from django.urls import path
from songs.views import views

urls = [
    path('songs/', views.SongList.as_view(), name='song-list'),
    # path('songs/<int:pk>/', views.SongDetail.as_view(), name='song-detail'),
    # path('songs/upload/', views.SongUpload.as_view(), name='song-upload'),
]