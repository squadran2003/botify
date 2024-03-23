from songs.models import Song
from django import forms


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', "file", "is_audio", "is_video"]