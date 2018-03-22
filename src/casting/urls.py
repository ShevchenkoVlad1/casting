# -*- coding: utf-8 -*-
from django.urls import path

from casting.models import Person, LikeDislike
from casting.views import HomeView, casting, person_list, subscribe, \
    VotesView, cast_likes

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('casting/', casting, name='casting'),

    path('subscribe/', subscribe, name='subscribe'),

    path('person_list/', person_list, name='person_list'),

    path('cast_likes/', cast_likes, name='cast_likes'),

    path('api/person/<pk>/like/',
         VotesView.as_view(model=Person, vote_type=LikeDislike.LIKE),
         name='person_like'),
    path('api/person/<pk>/dislike/',
         VotesView.as_view(model=Person, vote_type=LikeDislike.DISLIKE),
         name='person_dislike'),

]
