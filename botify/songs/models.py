from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def songs_directory_path(instance, filename):
    return 'songs/user_{0}_{1}'.format(instance.artist.id, filename)


def thumbnail_directory_path(instance, filename):
    return 'thumbnails/user_{0}_{1}'.format(instance.artist.id, filename)


class Song(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    thumbnail = models.ImageField(
        upload_to=thumbnail_directory_path,
        width_field='thumbnail_width',
        height_field='thumbnail_height',
        null=True, blank=True
    )
    thumbnail_width = models.IntegerField(default=1280)
    thumbnail_height = models.IntegerField(default=720)
    file = models.FileField(upload_to=songs_directory_path)
    is_audio = models.BooleanField(default=True)
    is_video = models.BooleanField(default=False)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
