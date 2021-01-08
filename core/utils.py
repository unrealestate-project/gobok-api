import io

from PIL import Image
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


def process_image_data_from_request(request) -> bytes:
    mem_file: InMemoryUploadedFile = request.FILES.get('file', None)
    if not mem_file:
        raise FileNotFoundError('File not found in the request')
    mem_file.file.seek(0)  # reset stream to initial position
    return mem_file.file.read()


def convert_bytes_image_to_bytes_thumbnail(original_image: bytes) -> bytes:
    image = Image.open(io.BytesIO(original_image))
    resized = image.resize(settings.THUMBNAIL_DIMENSION)
    buf = io.BytesIO()
    resized.save(buf, format='JPEG')
    return buf.getvalue()


def convert_image_to_thumbnail(original_image):
    image = Image.open(original_image)
    image.thumbnail(settings.THUMBNAIL_DIMENSION, Image.ANTIALIAS)
    thumb_obj = io.BytesIO()
    image.save(thumb_obj, format='JPEG')
    return thumb_obj
