from django.db.models.signals import post_delete  # Import the post_delete signal
from django.dispatch import receiver

from songs.models import Song

@receiver(post_delete, sender=Song)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)
