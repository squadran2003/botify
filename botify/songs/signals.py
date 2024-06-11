from django.db.models.signals import post_delete, post_save # Import the post_delete signal
from django.dispatch import receiver
from django.conf import settings
from songs.models import Song, TempThumbnail
from songs.forms import TempThumbnailForm
from songs.thumbnail_creator import ThumbnailCreator
from moviepy.editor import VideoFileClip
from PIL import Image
import os


@receiver(post_save, sender=Song)
def my_handler(sender, **kwargs):
    song = kwargs['instance']
    if song.thumbnail:
        print('Thumbnail already exists')
        for temp_thumbnail in song.tempthumbnail_set.all():
            path = temp_thumbnail.thumbnail.path
            os.remove(path)
            temp_thumbnail.delete()
        return
    if settings.DEBUG:
        clip = VideoFileClip(song.file.path)
    else:
        clip = VideoFileClip(song.file.url)
    # Get the duration of the video in seconds
    duration = int(clip.duration)

    # Loop through the video and save thumbnails
    interval = 1
    for t in range(0, min(duration, 10), interval):
        # Get the frame at time t
        frame = clip.get_frame(t)

        # Convert the frame to an image
        frame_image = Image.fromarray(frame)

        frame_image = frame_image.resize((1280, 720))
        path = f"{settings.MEDIA_ROOT}/thumbnails/temp/user_{song.id}_{t}.png"
        if settings.DEBUG:
            frame_image.save(path)
        else:
            # save to s3
            import boto3
            s3 = boto3.client('s3')
            path = f"/thumbnails/temp/user_{song.id}_{t}.png"
            # save to in memory
            import io
            frame_image = io.BytesIO()
            # here is the problem
            s3.upload_fileobj(frame_image, 'botifywebapp', path)
            # get a normal url
        TempThumbnail.objects.create(song=song, thumbnail=path)
