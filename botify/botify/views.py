from django.shortcuts import render
from songs.models import Song


def index(request):
    songs = Song.objects.all().prefetch_related('artist')
    return render(request, "index.html", {'songs': songs})