import os

from django.db import models


def get_person_photo_path(instance, filename):
    return os.path.join('person_photos', str(instance.person_id), filename)


def get_worker_photo_path(instance, filename):
    return os.path.join('worker_photos', str(instance.position), filename)


def get_poster_photo_path(instance, filename):
    return os.path.join('poster_photos', str(instance.title), filename)


def get_film_photo_path(instance, filename):
    return os.path.join('film_photos', str(instance.title), filename)


class Poster(models.Model):
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to=get_poster_photo_path, blank=True,
                              null=True)
    about_info = models.TextField(max_length=1000, blank=True)


class Worker(models.Model):
    position = models.CharField(max_length=250)
    about_info = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to=get_worker_photo_path, blank=True,
                              null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None)
    age = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    prof = models.CharField(max_length=70)
    experience = models.TextField(max_length=1000, blank=True)
    grouping = models.BooleanField(default=False)
    crowd_scene = models.BooleanField(default=False)
    about_info = models.TextField(max_length=1000, blank=True)
    video_url = models.CharField(max_length=70, blank=True)

    is_main = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class PersonPhoto(models.Model):
    person = models.ForeignKey(Person, default=None, on_delete=None)
    photo = models.ImageField(upload_to=get_person_photo_path, blank=True,
                              null=True)


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=250, null=True)
    video_id = models.CharField(max_length=70)


class FilmPhoto(models.Model):
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to=get_film_photo_path, blank=True,
                              null=True)
