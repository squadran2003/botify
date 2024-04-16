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

@receiver(post_save, sender=Song)
def post_save_processing(sender, instance, **kwargs):
    if instance.thumbnail:
        # if in production we will want to store in temp and upload to s3
        if not settings.DEBUG:
            response = requests.get(instance.thumbnail.url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((600, 800))
            img.save(instance.thumbnail.path)
        else:
            # resize the image
            img = Image.open(instance.thumbnail.path)
            img = resize_image_with_aspect_ratio(img, 600, 800)
            path = instance.thumbnail.path
            img.save(path)


def resize_image_with_aspect_ratio(image, max_width, max_height):
    """
    Resize the image to fit within the specified maximum width and height,
    preserving the aspect ratio.
    """
    # Calculate aspect ratio
    width, height = image.size
    aspect_ratio = width / height

    # Determine new size while preserving aspect ratio
    if width > max_width or height > max_height:
        if aspect_ratio > 1:  # Landscape orientation
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:  # Portrait or square orientation
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_image
    else:
        return image  # No nee
