from django.shortcuts import render
from django.conf import settings
from songs.forms import SongForm
from songs.models import Song
from django.shortcuts import render, redirect
from django.contrib import messages


def handel_uploaded_file(f):
    path = settings.MEDIA_ROOT + '/songs/{}'.format(f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def SongUpload(request):
    if request.user.is_anonymous:
        messages.error(request, 'You need to login to upload songs.')
        return redirect('users:login')
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            handel_uploaded_file(request.FILES['file'])
            form.save()
            messages.success(request, 'Song uploaded succssfully.')
            return redirect('home')
        else:
            print(form.errors)
            return render(request, 'songs/upload_song.html', {'form': form})
    else:
        form = SongForm()
        form.fields['artist'].initial = request.user
    return render(request, 'songs/upload_song.html', {'form': form})


def SongDetail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'songs/song_detail.html', {'song': song})
