from django.contrib import admin

from casting.models import Person, Image


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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('person', 'image')

    search_fields = ['person']

    fields = ('person', 'image',)
