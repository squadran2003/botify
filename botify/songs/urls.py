from django.urls import path
from songs import views

urlpatterns = [
    # path('songs/', SongList.as_view(), name='song-list'),
    # path('songs/<int:pk>/', views.SongDetail.as_view(), name='song-detail'),
    path('songs/upload/', views.SongUpload, name='upload'),
]