from django.db.models.signals import post_delete, post_save # Import the post_delete signal
from django.dispatch import receiver

from songs.models import Song

@receiver(post_delete, sender=Song)
def post_delete_processing(sender, instance, **kwargs):
    instance.thumbnail.delete(False)
    instance.file.delete(False)

# @receiver(post_save, sender=Song)
# def post_save_processing(sender, instance, **kwargs):
#     if instance.thumbnail:
#         from PIL import Image
#         # resize the image
#         img = Image.open(instance.thumbnail.path)
#         img = img.resize((1280, 720))
#         path = instance.thumbnail.path
#         instance.thumbnail.delete(False)
#         # print(instance.thumbnail.path)
#         print(img.size)
#         img.save(path)