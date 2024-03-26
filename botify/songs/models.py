from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Song(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    is_audio = models.BooleanField(default=True)
    is_video = models.BooleanField(default=False)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

