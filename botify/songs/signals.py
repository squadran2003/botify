from django.db.models.signals import post_delete, post_save # Import the post_delete signal
from django.dispatch import receiver
from PIL import Image
import requests
from io import BytesIO
from django.conf import settings


from songs.models import Song

@receiver(post_delete, sender=Song)
def post_delete_processing(sender, instance, **kwargs):
    instance.thumbnail.delete(False)
    instance.file.delete(False)


