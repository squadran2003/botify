from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    is_audio = models.BooleanField(default=True)
    is_video = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def clean(self):
        if self.file:
            if self.file.size > 4*1024*1024:
                raise ValidationError("File too large ( > 4mb )")
            if not self.file.name.endswith(
                ('.mp3', '.mp4', '.wav', '.flac', '.m4a', '.wma', '.aac', '.ogg', '.webm', '.mkv', '.avi', '.mov', '.wmv')
            ):
                raise ValidationError("Content-Type is not audio or video")
            self.file.name = str(self.user.id) + '_'+self.file.name
            return self.file
        else:
            raise ValidationError("Couldn't read uploaded file")