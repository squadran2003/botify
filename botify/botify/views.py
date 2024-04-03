from django.shortcuts import render, redirect
from songs.models import Song


def index(request):
    if not request.user.is_authenticated:
        return render(request, "index.html")
    songs = Song.objects.all().prefetch_related('artist')
    return render(request, "dashboard.html", {'songs': songs})