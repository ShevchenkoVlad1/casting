from django.urls import path

from casting.views import home, casting, person_list, subscribe

urlpatterns = [
    path('', home, name='home'),

    path('casting/', casting, name='casting'),

    path('subscribe/', subscribe, name='subscribe'),

    path('person_list/', person_list, name='person_list')
]
