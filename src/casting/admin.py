from django.contrib import admin

from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, \
    Film_about, FilmPhoto, Partner, Social, UserIP


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

    readonly_fields = ('Likes',)

    fields = ('first_name', 'second_name', 'email', 'phone', 'age',
              'city', 'gender', 'prof', 'experience', 'grouping',
              'crowd_scene', 'about_info', 'video_url', 'Likes', 'is_main',)


@admin.register(UserIP)
class UserIPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'user_data', 'created_date',)
    readonly_fields = ('ip', 'user_data', 'created_date',)
    fields = ('ip', 'user_data', 'created_date',)


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
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('position', 'about_info', 'photo', 'languages', 'is_main',)
    fields = ('position', 'about_info', 'photo', 'languages', 'is_main',)


@admin.register(Film_about)
class FilmAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_info', 'photo', 'languages',)
    fields = ('title', 'about_info', 'photo', 'languages',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner_url', 'photo',)
    fields = ('title', 'partner_url', 'photo',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'social_id', 'social_url',)
    fields = ('title', 'social_id', 'social_url',)
    readonly_fields = ('title',)
