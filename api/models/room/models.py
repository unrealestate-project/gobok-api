from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel


class Room(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    bumped_at = models.DateTimeField(default=timezone.now)  # 끌올
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-bumped_at']
