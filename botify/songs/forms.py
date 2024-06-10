from songs.models import Song, Comment, TempThumbnail
from django import forms
from django.core.exceptions import ValidationError


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', "description", "artist", "thumbnail", "file", "is_audio", "is_video"]
        help_texts = {
            'thumbnail': 'Upload a thumbnail for the song',
            'file': 'Upload a song file'
        }

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'block w-full rounded-md border-0 py-3 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 mt-4', 
             'placeholder': 'Song Title'
             }
        )
        self.fields['description'].widget.attrs.update(
            {
             'class': 'block w-full rounded-md border-0 py-3 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 mt-4', 
             'placeholder': 'Add a description'
            }
        )
        # self.fields['thumbnail'].widget.attrs.update({"help_texts": "Upload a thumbnail for the song"})
        # self.fields['file'].widget.attrs.update({"help_texts": "Upload a song file"})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
        self.fields['is_audio'].widget.attrs.update({'class': 'checkbox'})
        self.fields['is_video'].widget.attrs.update({'class': 'checkbox'})
        self.fields['artist'].widget = forms.HiddenInput()

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        # convert the file size like 108466176 to GB
        size = file.size / (1024 * 1024 * 1024)
        if size > 1:
            raise ValidationError("File too large ( > 1GB )")
        if not file.name.endswith(
            ('.mp3', '.mp4', '.wav', '.flac', '.m4a', '.wma', '.aac', '.ogg', '.webm', '.mkv', '.avi', '.mov', '.wmv')
        ):
            raise ValidationError("Not supported audo video file format.")
        return file


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        help_texts = {
            'content': 'Add a comment',

        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': '4',
                    'placeholder': 'Add a comment', 
                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}
            ),
        }


class TempThumbnailForm(forms.ModelForm):
    class Meta:
        model = TempThumbnail
        fields = ['song', 'thumbnail']
        help_texts = {
            'thumbnail': 'Upload a thumbnail for the song',
        }
        widgets = {
            'thumbnail': forms.FileInput(
                attrs={
                    'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
                }
            )
        }
