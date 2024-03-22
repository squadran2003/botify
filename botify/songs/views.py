from django.shortcuts import render
from songs.forms import SongForm


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SongForm()
    return render(request, 'upload_song.html', {'form': form})
