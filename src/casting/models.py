# -*- coding: utf-8 -*-
import os

from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _


def get_person_photo_path(instance, filename):
    return os.path.join('person_photos', str(instance.person_id), filename)


def get_worker_photo_path(instance, filename):
    return os.path.join('worker_photos', str(instance.position), filename)


def get_poster_photo_path(instance, filename):
    return os.path.join('poster_photos', str(instance.title), filename)


def get_film_photo_path(instance, filename):
    return os.path.join('film_photos', str(instance.title), filename)


def get_partner_photo_path(instance, filename):
    return os.path.join('partner_photos', str(instance.title), filename)


class FilmAbout(models.Model):
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to=get_poster_photo_path, blank=True,
                              null=True)
    about_info = models.TextField(max_length=8000, blank=True)
    languages = models.CharField(max_length=128, unique=False,
                                 choices=(
                                     ('ua', _('Ukrainian')),
                                     ('en', _('English')),
                                 ), default=('ua', _('Ukrainian')))


class Worker(models.Model):
    position = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    about_info = models.TextField(max_length=8000, blank=True)
    photo = models.ImageField(upload_to=get_worker_photo_path, blank=True,
                              null=True)
    languages = models.CharField(max_length=128, unique=False,
                                 choices=(
                                     ('ua', _('Ukrainian')),
                                     ('en', _('English')),
                                 ), default=('ua', _('Ukrainian')))
    is_main = models.BooleanField(default=False)


class UserIP(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    user_data = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def persons(self):
        return self.get_queryset().filter(
            content_type__model='persons').order_by('-created_date')


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, _("Dislike")),
        (LIKE, _("Like"))
    )

    vote = models.SmallIntegerField(verbose_name=_("Vote"), choices=VOTES)
    user = models.ForeignKey(UserIP, verbose_name=_("User"),
                             on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Person(models.Model):
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=35)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None)
    age = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    prof = models.CharField(max_length=70)
    experience = models.TextField(max_length=8000, blank=True)
    grouping = models.BooleanField(default=False)
    crowd_scene = models.BooleanField(default=False)
    about_info = models.TextField(max_length=8000, blank=True)
    video_url = models.CharField(max_length=150, blank=True)
    votes = GenericRelation(LikeDislike, related_query_name='persons')
    images = models.CharField(max_length=150, default=None, null=True,
                              blank=True)
    is_main = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class PersonPhoto(models.Model):
    person = models.ForeignKey(Person, default=None, on_delete=None,
                               unique=False, related_name='photos')
    photo = models.ImageField(upload_to=get_person_photo_path, blank=True,
                              null=True)

    def __str__(self):
        return str(self.photo)


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=250, null=True)
    video_id = models.CharField(max_length=70)


class FilmPhoto(models.Model):
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to=get_film_photo_path, blank=True,
                              null=True)


class Partner(models.Model):
    title = models.CharField(max_length=250, null=True)
    photo = models.ImageField(upload_to=get_partner_photo_path, blank=True,
                              null=True)
    partner_url = models.CharField(max_length=150, blank=True)


class Social(models.Model):
    title = models.CharField(max_length=250, unique=True)
    social_id = models.CharField(max_length=150, blank=True)
    social_url = models.CharField(max_length=150, blank=True)
