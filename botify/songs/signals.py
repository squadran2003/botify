from django.db.models.signals import post_delete, post_save # Import the post_delete signal
from django.dispatch import receiver

from songs.models import Song

@receiver(post_delete, sender=Song)
def post_delete_processing(sender, instance, **kwargs):
    instance.thumbnail.delete(False)
    instance.file.delete(False)

# @receiver(post_save, sender=Song)
# def post_save_processing(sender, instance, **kwargs):
#     if instance.file:
#         from pyffmpeg import FFmpeg
#         ff = FFmpeg()
#         ff.convert(instance.file, instance.placeholder_image, [f'-ss {instance.file.duration // 2}', '-vframes 1'])
#         instance.placeholder_image.save(instance.placeholder_image.name, instance.placeholder_image.file, save=False)

