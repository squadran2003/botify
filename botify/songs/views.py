from django.shortcuts import render
from songs.forms import SongForm


def SongUpload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SongForm()
    return render(request, 'songs/upload_song.html', {'form': form})
