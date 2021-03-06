# -*- coding: utf-8 -*-
from django.contrib import admin

from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, \
    FilmAbout, FilmPhoto, Partner, Social, UserIP, CastingRules, CastingNews

from django_summernote.admin import SummernoteModelAdmin


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    @staticmethod
    def Likes(obj):
        return '{}'.format(obj.votes.sum_rating())

    list_display = ('first_name', 'second_name', 'email', 'phone', 'age',
                    'city', 'gender', 'prof', 'experience', 'grouping',
                    'crowd_scene', 'about_info', 'video_url', 'Likes',
                    'is_main',)

    list_filter = ['city', 'gender', 'prof', 'grouping', 'crowd_scene']

    search_fields = ['experience', 'about_info', 'is_main']

    readonly_fields = ('Likes', 'images',)

    fields = ('first_name', 'second_name', 'email', 'phone', 'age',
              'city', 'gender', 'prof', 'experience', 'grouping',
              'crowd_scene', 'about_info', 'video_url', 'images', 'Likes',
              'is_main',)


@admin.register(UserIP)
class UserIPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'user_data', 'last_login', 'created_date',)
    readonly_fields = ('ip', 'user_data', 'last_login', 'created_date',)
    fields = ('ip', 'user_data', 'last_login', 'created_date',)


@admin.register(PersonPhoto)
class PersonPhotoAdmin(admin.ModelAdmin):
    list_display = ('person', 'photo',)
    search_fields = ['person']
    fields = ('person', 'photo',)


@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id',)
    fields = ('title', 'video_id',)


@admin.register(FilmPhoto)
class FilmPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo',)
    fields = ('title', 'photo',)


@admin.register(Worker)
class WorkerAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_info',)
    list_display = ('position', 'name', 'about_info', 'photo', 'languages',
                    'is_main',)
    fields = ('position', 'name', 'about_info', 'photo', 'languages',
              'is_main',)


@admin.register(FilmAbout)
class FilmAboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_info',)
    list_display = ('title', 'about_info', 'photo', 'languages',)
    fields = ('title', 'about_info', 'photo', 'languages',)


@admin.register(CastingRules)
class CastingRulesAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_info',)
    list_display = ('about_info', 'languages',)
    fields = ('about_info', 'languages',)


@admin.register(CastingNews)
class CastingNewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_info',)
    list_display = ('title', 'about_info', 'photo', 'link', 'languages',)
    fields = ('title', 'about_info', 'photo', 'link', 'languages',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner_url', 'photo',)
    fields = ('title', 'partner_url', 'photo',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'social_id', 'social_url',)
    fields = ('title', 'social_id', 'social_url',)
    readonly_fields = ('title',)
