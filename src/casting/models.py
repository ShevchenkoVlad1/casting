# -*- coding: utf-8 -*-
import os

from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

time_as_folder = datetime.now().strftime('%Y/%m/%d')


def get_person_photo_path(instance, filename):
    return os.path.join('person_photos', time_as_folder, filename)


def get_worker_photo_path(instance, filename):
    return os.path.join('worker_photos', time_as_folder, filename)


def get_poster_photo_path(instance, filename):
    return os.path.join('poster_photos', time_as_folder, filename)


def get_film_photo_path(instance, filename):
    return os.path.join('film_photos', time_as_folder, filename)


def get_partner_photo_path(instance, filename):
    return os.path.join('partner_photos', time_as_folder, filename)


class FilmAbout(models.Model):
    title = models.CharField(max_length=250, null=True,
                             verbose_name=_('Title'))
    photo = models.ImageField(upload_to=get_poster_photo_path, blank=True,
                              null=True, verbose_name=_('Photo'))
    about_info = models.TextField(max_length=8000, blank=True,
                                  verbose_name=_('About info'))
    languages = models.CharField(max_length=128, unique=False,
                                 choices=(
                                     ('ua', _('Ukrainian')),
                                     ('en', _('English')),
                                 ), default=('ua', _('Ukrainian')),
                                 verbose_name=_('languages'))

    class Meta:
        verbose_name = _('About film')
        verbose_name_plural = _('About film')


class Worker(models.Model):
    position = models.CharField(max_length=250, verbose_name=_('Position'))
    name = models.CharField(max_length=250, verbose_name=_('Name'))
    about_info = models.TextField(max_length=8000, blank=True,
                                  verbose_name=_('About info'))
    photo = models.ImageField(upload_to=get_worker_photo_path, blank=True,
                              null=True, verbose_name=_('Photo'))
    languages = models.CharField(max_length=128, unique=False,
                                 choices=(
                                     ('ua', _('Ukrainian')),
                                     ('en', _('English')),
                                 ), default=('ua', _('Ukrainian')),
                                 verbose_name=_('Languages'))
    is_main = models.BooleanField(default=False, verbose_name=_('Is main'))

    class Meta:
        verbose_name = _('Workers')
        verbose_name_plural = _('Workers')


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
    first_name = models.CharField(max_length=70, verbose_name=_('First name'))
    second_name = models.CharField(max_length=35,
                                   verbose_name=_('Second name'))
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None,
                             verbose_name=_('Phone'))
    age = models.DateField(null=True, blank=True, verbose_name=_('Age'))
    city = models.CharField(max_length=70, verbose_name=_('City'))
    gender = models.CharField(max_length=70, verbose_name=_('Gender'))
    prof = models.CharField(max_length=70, verbose_name=_('Professionalism'))
    experience = models.TextField(max_length=8000, blank=True,
                                  verbose_name=_('Experience'))
    grouping = models.BooleanField(default=False, verbose_name=_('Grouping'))
    crowd_scene = models.BooleanField(default=False,
                                      verbose_name=_('Crowd scene'))
    about_info = models.TextField(max_length=8000, blank=True,
                                  verbose_name=_('About info'))
    video_url = models.CharField(max_length=150, blank=True,
                                 verbose_name=_('Video url'))
    votes = GenericRelation(LikeDislike, related_query_name='persons',
                            verbose_name=_('Votes'))
    images = models.CharField(max_length=150, default=None, null=True,
                              blank=True, verbose_name=_('Images'))
    is_main = models.BooleanField(default=False, verbose_name=_('Is main'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Created date'))

    class Meta:
        verbose_name = _('Persons')
        verbose_name_plural = _('Persons')


class PersonPhoto(models.Model):
    person = models.ForeignKey(Person, default=None, on_delete=None,
                               unique=False, related_name='photos',
                               verbose_name=_('Person'))
    photo = models.ImageField(upload_to=get_person_photo_path, blank=True,
                              null=True, verbose_name=_('Photo'))

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = _('Person photos')
        verbose_name_plural = _('Person photos')


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=250, null=True,
                             verbose_name=_('Title'))
    video_id = models.CharField(max_length=70, verbose_name=_('Video id'))

    class Meta:
        verbose_name = _('Youtube videos')
        verbose_name_plural = _('Youtube videos')


class FilmPhoto(models.Model):
    title = models.CharField(max_length=250, null=True,
                             verbose_name=_('Title'))
    photo = models.ImageField(upload_to=get_film_photo_path, blank=True,
                              null=True, verbose_name=_('Photo'))

    class Meta:
        verbose_name = _('Film photos')
        verbose_name_plural = _('Film photos')


class Partner(models.Model):
    title = models.CharField(max_length=250, null=True,
                             verbose_name=_('Title'))
    photo = models.ImageField(upload_to=get_partner_photo_path, blank=True,
                              null=True, verbose_name=_('Photo'))
    partner_url = models.CharField(max_length=150, blank=True,
                                   verbose_name=_('Partner url'))

    class Meta:
        verbose_name = _('Partners')
        verbose_name_plural = _('Partners')


class Social(models.Model):
    title = models.CharField(max_length=250, unique=True,
                             verbose_name=_('Title'))
    social_id = models.CharField(max_length=150, blank=True,
                                 verbose_name=_('Social id'))
    social_url = models.CharField(max_length=150, blank=True,
                                  verbose_name=_('Social url'))

    class Meta:
        verbose_name = _('Socials')
        verbose_name_plural = _('Socials')
