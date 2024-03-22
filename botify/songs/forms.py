from songs.models import Song
from django import forms

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'release_date', 'genre', 'duration', 'lyrics']