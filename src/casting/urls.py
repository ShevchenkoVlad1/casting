from django.urls import path

from casting.views import home, casting, person_list

urlpatterns = [
    path('', home, name='home'),

    path('casting/', casting, name='casting'),

    path('person_list/', person_list, name='person_list')
]
