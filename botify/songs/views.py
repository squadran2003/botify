from django.shortcuts import render
from songs.forms import SongForm
from django.shortcuts import render, redirect
from django.contrib import messages


def SongUpload(request):
    if request.user.is_anonymous:
        messages.error(request, 'You need to login to upload songs.')
        return redirect('users:login')
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song uploaded succssfully.')
            return redirect('home')
        else:
            return redirect("songs:upload", {'form': form})
    else:
        form = SongForm()
        form.fields['artist'].initial = request.user
    return render(request, 'songs/upload_song.html', {'form': form})
