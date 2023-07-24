from django.db import models
from django.dispatch import receiver

from menu.models import ImageMenu


@receiver(models.signals.post_delete, sender=ImageMenu)
def delete_image_on_update(sender, instance, **kwargs):
    pass
