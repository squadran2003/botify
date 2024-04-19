from django.shortcuts import render
from django.conf import settings
from songs.forms import SongForm, CommentForm
from songs.models import Song, Like
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
            print(form.errors)
            return render(request, 'songs/upload_song.html', {'form': form})
    else:
        form = SongForm()
        form.fields['artist'].initial = request.user
    return render(request, 'songs/upload_song.html', {'form': form})


def SongDetail(request, pk):
    song = Song.objects.get(id=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.song = song
            comment.user = request.user
            comment.save()
            return redirect('songs:detail', pk)
    return render(request, 'songs/song_detail.html', {'song': song, 'comment_form': comment_form})


def LikeSong(request, song_id):
    if request.user.is_anonymous:
        messages.error(request, 'You need to login to like songs.')
        return redirect('users:login')
    try:
        song = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        messages.error(request, 'Invalid song id')
        return redirect('songs:detail', song_id)
    else:
        like, created = Like.objects.get_or_create(
            user=request.user, song=song
        )
    if not created:
        like.delete()
    return redirect('songs:detail', song_id)