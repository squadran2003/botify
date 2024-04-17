from django.shortcuts import render, redirect
from songs.models import Song


def index(request, media="v"):
    if media == "v":
        songs = Song.objects.filter(
            is_video=True
        ).prefetch_related('artist', 'like_set')
        # add audio video active classes to the context to toggle the dropdown
        return render(request, "index_video.html", {
                'songs': songs, 'audio_active': '',
                'video_active': 'is-active'
            }
        )
    else:
        songs = Song.objects.filter(
            is_audio=True
        ).prefetch_related('artist', 'like_set')
        return render(request, "index_audio.html", {
                'songs': songs, 'video_active': '',
                'audio_active': 'is-active'
            }
        )