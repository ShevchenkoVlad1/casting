import os

from django.db import models
from datetime import datetime


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Person(models.Model):
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None)
    age = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    prof = models.CharField(max_length=70)
    experience = models.TextField(max_length=1000, blank=True, null=True)
    grouping = models.BooleanField(default=False)
    crowd_scene = models.BooleanField(default=False)
    about_info = models.TextField(max_length=1000, blank=True, null=True)
    contact_image = models.ImageField(upload_to=get_image_path, blank=True,
                                      null=True)
    video_url = models.CharField(max_length=70)

    is_main = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())
