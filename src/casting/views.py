# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.translation import get_language
from django.views import View
from django.views.decorators.http import require_POST, require_GET

from casting.forms import PersonForm, ImageForm
from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, \
    FilmAbout, FilmPhoto, Partner, Social, UserIP, LikeDislike, CastingRules, \
    CastingNews


class HomeView(View):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        if not UserIP.objects.filter(ip=ip).exists():
            get_user_data = request.META.get('HTTP_USER_AGENT')

            user = UserIP()
            user.ip = ip
            user.created_date = datetime.now()
            user.last_login = datetime.now()
            user.user_data = get_user_data
            user.save()
            is_welcome = True
        else:
            UserIP.objects.filter(ip=ip).update(last_login=datetime.now())
            is_welcome = False

        current_lang = get_language()

        person_list = sorted(Person.objects.filter(is_main=1),
                             key=lambda p: p.votes.sum_rating(), reverse=True)
        youtube_list = YoutubeVideo.objects.all()

        crew_list = Worker.objects.filter(languages=current_lang)
        main_in_crew = crew_list.filter(is_main=1)
        crew = crew_list.filter(is_main=0)

        film_about = FilmAbout.objects.filter(languages=current_lang
                                              ).order_by('-id')[:1]
        casting_rules = CastingRules.objects.filter(languages=current_lang
                                                    ).order_by('-id')[:1]
        news_list = CastingNews.objects.filter(languages=current_lang)
        film_photo_list = FilmPhoto.objects.all()
        partner_list = Partner.objects.all()

        image_form = ImageForm

        # social
        instagram = Social.objects.filter(title="Instagram").get()
        youtube = Social.objects.filter(title="YouTube").get()
        facebook = Social.objects.filter(title="Facebook").get()
        imdb = Social.objects.filter(title="Imdb").get()
        wikipedia = Social.objects.filter(title="Wikipedia").get()

        context = {
            'person_list': person_list,
            'youtube_list': youtube_list,
            'main_in_crew': main_in_crew,
            'crew': crew,
            'film_about': film_about,
            'news_list': news_list,
            'casting_rules': casting_rules,
            'film_photo_list': film_photo_list,
            'instagram': instagram,
            'youtube': youtube,
            'facebook': facebook,
            'imdb': imdb,
            'wikipedia': wikipedia,
            'partner_list': partner_list,
            'image_form': image_form,
            'is_welcome': is_welcome
        }

        return render(request, 'casting/index.html', context)


def save_file(file):
    filename = file._get_name()
    fd = open('%s' % (os.path.join(settings.MEDIA_ROOT,
                                   'person_photos', str(filename))), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


@require_POST
def casting(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST)

        if person_form.is_valid():
            person = Person()
            person.first_name = request.POST['first_name']
            person.second_name = request.POST['second_name']
            person.email = request.POST['email']
            person.phone = request.POST['phone']
            person.age = request.POST['age']
            person.city = request.POST['city']
            person.gender = request.POST['gender']
            person.prof = request.POST['prof']
            person.experience = request.POST['experience']
            person.crowd_scene = request.POST['crowd_scene']
            person.grouping = request.POST['grouping']
            person.about_info = request.POST['about_info']
            person.video_url = request.POST['video_url']

            images = ''
            person.save()
            for image in request.FILES.getlist('contact_image'):
                save_file(image)
                photo = PersonPhoto(
                    person=person,
                    photo='person_photos/%s' % image._get_name())
                images += '/media/person_photos/%s\n' % image._get_name()

                photo.save()
            person.images = images
            person.save()

            # Email sending
            email = request.POST['email']

            email_title = 'Casting | Registered'
            context = {
                'first_name': request.POST['first_name']
            }
            email_message = render_to_string('casting/email_registered.html',
                                             context)
            to_email = '{}'.format(email)

            if settings.EMAIL_FAKE == 'yes':
                print(email_message)
            else:
                email_sending = EmailMessage(email_title, email_message,
                                             to=[to_email])
                email_sending.send()

    return HttpResponse()


@require_POST
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['subscribe-email']

        email_title = 'Casting | subscribe'
        context = {}
        email_message = render_to_string('casting/email_subscribe.html',
                                         context)
        to_email = '{}'.format(email)

        if settings.EMAIL_FAKE == 'yes':
            print(email_message)
        else:
            email_sending = EmailMessage(email_title, email_message,
                                         to=[to_email])
            email_sending.send()
    return HttpResponse()


@require_GET
def person_list(request):
    if request.method == 'GET':
        person_id = request.GET.get('person_id', None)
        person = Person.objects.filter(id=person_id).get()
        if person.photos.all:
            contact_image = ''
            for photo in person.photos.all():
                contact_image += '%s\n' % photo
        else:
            contact_image = '/media/photos/noimage.png'
        data = {
            'id': person.id,
            'first_name': person.first_name,
            'second_name': person.second_name,
            'email': person.email,
            'phone': person.phone,
            'age': person.age,
            'city': person.city,
            'gender': person.gender,
            'prof': person.prof,
            'experience': person.experience,
            'crowd_scene': person.crowd_scene,
            'grouping': person.grouping,
            'about_info': person.about_info,
            'contact_image': contact_image,
            'video_url': person.video_url,
            'like_count': person.votes.likes().count(),
            'like_sum': person.votes.sum_rating()
        }
        return JsonResponse(data)


class VotesView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        userip = get_object_or_404(UserIP, ip=ip)
        obj = self.model.objects.get(pk=pk)
        try:
            likedislike = LikeDislike.objects.get(
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id, user=userip)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=userip, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )


@require_GET
def cast_likes(request):
    if request.method == 'GET':
        person_id = request.GET.get('person_id', None)
        person = Person.objects.filter(id=person_id).get()
        data = {
            'id': person.id,
            'cast_likes': person.votes.sum_rating()
        }
        return JsonResponse(data)
