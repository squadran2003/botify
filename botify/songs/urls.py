from django.urls import path
from songs import views

urlpatterns = [
    # path('songs/', SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', views.SongDetail, name='detail'),
    path('songs/<int:song_id>/like/', views.LikeSong, name='like'),
    path('upload/', views.SongUpload, name='upload'),
]