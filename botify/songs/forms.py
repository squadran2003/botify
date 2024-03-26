from songs.models import Song
from django import forms
from django.core.exceptions import ValidationError


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', "artist", "file", "is_audio", "is_video"]

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Song Title'}
        )
        self.fields['file'].widget.attrs.update({'class': 'file-input'})
        self.fields['is_audio'].widget.attrs.update({'class': 'checkbox', 'help_text': 'Is this an audio file?'})
        self.fields['is_video'].widget.attrs.update({'class': 'checkbox'})
        self.fields['artist'].widget = forms.HiddenInput()

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file.size > 4*1024*1024:
            raise ValidationError("File too large ( > 4mb )")
        if not file.name.endswith(
            ('.mp3', '.mp4', '.wav', '.flac', '.m4a', '.wma', '.aac', '.ogg', '.webm', '.mkv', '.avi', '.mov', '.wmv')
        ):
            raise ValidationError("Not supported audo video file format.")
        return file
