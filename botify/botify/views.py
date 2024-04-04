from django.shortcuts import render, redirect
from songs.models import Song


def index(request, type="v"):
    if type == "v":
        songs = Song.objects.filter(
            is_video=True
        ).prefetch_related('artist')
    else:
        songs = Song.objects.filter(
            is_audio=True
        ).prefetch_related('artist')
    return render(request, "index.html", {'songs': songs})