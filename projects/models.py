# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import pre_delete, post_save, post_init
from django.dispatch.dispatcher import receiver


class Project(models.Model):
    proj_name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    website = models.TextField(default='', blank=True)
    repository = models.TextField(default='', blank=True)
    start_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='project_images', default=None)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})


@receiver(post_init, sender=Project)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.image


@receiver(post_save, sender=Project)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.image.path:
            instance._current_image_file.delete(False)


# Receive the pre_delete signal and delete the file associated with the model instance.
@receiver(pre_delete, sender=Project)
def project_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.image:
        instance.image.delete(False)


def __str__(self):
    return self.proj_name
