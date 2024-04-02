from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Song(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    file = models.FileField(upload_to='songs/')
    is_audio = models.BooleanField(default=True)
    is_video = models.BooleanField(default=False)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
