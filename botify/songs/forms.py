from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from songs.models import Song
from django import forms



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', "file", "is_audio", "is_video"]
    
    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': ''})
        self.fields['artist'].widget.attrs.update({'class': ''})
        self.fields['file'].widget.attrs.update({'class': ''})
        self.fields['is_audio'].widget.attrs.update({'class': ''})
        self.fields['is_video'].widget.attrs.update({'class': ''})