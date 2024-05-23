import tempfile
from django.test import TestCase
from django.http import HttpRequest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from songs.forms import SongForm
from PIL import Image
import io


class TestSongForms(TestCase):
    def setUp(self) -> None:
        # create a user and log them in
        User = get_user_model()
        self.user = User.objects.create_user(email='test@test.com', password='test')

    def test_song_form_valid_when_all_fields_are_submitted(self):
        with tempfile.NamedTemporaryFile(suffix='.mp3') as temp_file, tempfile.NamedTemporaryFile(suffix='.jpg') as temp_thumbnail:
            temp_file.write(b'Test content')
            temp_file.seek(0)
            
            image = Image.new('RGB', (100, 100))
            temp_thumbnail = io.BytesIO()
            image.save(temp_thumbnail, format='JPEG')
            temp_thumbnail.seek(0)
            # Create SimpleUploadedFile objects
            uploaded_file = SimpleUploadedFile(
                temp_file.name, temp_file.read(), content_type='audio/mp3'
            )
            uploaded_thumbnail = SimpleUploadedFile(
                'thumbnail.jpg', temp_thumbnail.read(), content_type='image/jpeg'
            )

            # Prepare request data
            request = HttpRequest()
            request.POST = {
                'user': self.user.id,
                'title': 'test',
                "description": "test description",
                'artist': self.user.id  # Assuming artist is also a user id or adjust accordingly
            }
            request.FILES = {
                'file': uploaded_file,
                'thumbnail': uploaded_thumbnail
            }
            request.user = self.user

            form = SongForm(request.POST, request.FILES)
            self.assertTrue(form.is_valid())

    def test_song_form_invalid_when_file_format_is_not_supported(self):
        with tempfile.NamedTemporaryFile(suffix='.mp2') as temp_file:
            temp_file.write(b'Test content')
            temp_file.seek(0)

            # Create a SimpleUploadedFile object
            uploaded_file = SimpleUploadedFile(
                temp_file.name,
                temp_file.read(),
                content_type='audio/mp3'
            )
            request = HttpRequest()
            request.POST = {
                'user': self.user,
                'title': 'test',
                'artist': self.user
            }
            request.FILES = {
                'file': uploaded_file
            }
            request.user = self.user
            form = SongForm(request.POST, request.FILES)
            self.assertEqual(
                form.errors['file'],
                ['Not supported audo video file format.']
            )