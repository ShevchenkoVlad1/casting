from django.contrib import admin

from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, Poster, \
    FilmPhoto


@admin.register(Person)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'phone', 'age',
                    'city', 'gender', 'prof', 'experience', 'grouping',
                    'crowd_scene', 'about_info', 'video_url',
                    'is_main',)

    list_filter = ['city', 'gender', 'prof', 'grouping', 'crowd_scene']

    search_fields = ['experience', 'about_info', 'is_main']

    fields = ('first_name', 'second_name', 'email', 'phone', 'age',
              'city', 'gender', 'prof', 'experience', 'grouping',
              'crowd_scene', 'about_info', 'video_url', 'is_main',)


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
    list_display = ('position', 'about_info', 'photo',)
    fields = ('position', 'about_info', 'photo',)


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'about_info', 'photo',)
    fields = ('title', 'about_info', 'photo',)
