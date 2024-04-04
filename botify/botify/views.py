from django.shortcuts import render, redirect
from songs.models import Song


def index(request, media="a"):
    if media == "v":
        songs = Song.objects.filter(
            is_video=True
        ).prefetch_related('artist')
        return render(request, "index_video.html", {'songs': songs})
    else:
        songs = Song.objects.filter(
            is_audio=True
        ).prefetch_related('artist')
        return render(request, "index_audio.html", {'songs': songs})