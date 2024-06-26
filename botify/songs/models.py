from django.db import models
from django.contrib.auth import get_user_model
import os
User = get_user_model()


def songs_directory_path(instance, filename):
    return 'songs/user_{0}_{1}'.format(instance.artist.id, filename)


def thumbnail_directory_path(instance, filename):
    return 'thumbnails/user_{0}_{1}'.format(instance.artist.id, filename)


def thumbnail_temp_directory_path(instance, filename):
    return 'thumbnails/temp/user_{0}_{1}'.format(instance.id, filename)


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


class TempThumbnail(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    thumbnail = models.ImageField(
        upload_to=thumbnail_temp_directory_path,
        width_field='thumbnail_width',
        height_field='thumbnail_height',
        null=True, blank=True
    )
    thumbnail_width = models.IntegerField(default=1280)
    thumbnail_height = models.IntegerField(default=720)

    def __str__(self):
        return f'Temp thumbnail for {self.song.title}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return f'{self.user.username} likes {self.song.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user.username} comments on {self.song.title}'




