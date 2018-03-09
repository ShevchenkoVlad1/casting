from django.conf import settings
from django.core.mail import EmailMessage
from django.forms import modelformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from casting.forms import PersonForm, ImageForm
from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, Poster, \
    FilmPhoto


def home(request):
    person_list = Person.objects.filter(is_main=1).order_by('-created_date')
    youtube_list = YoutubeVideo.objects.all()
    crew_list = Worker.objects.all()
    poster = Poster.objects.order_by('-id')[:1]
    film_photo_list = FilmPhoto.objects.all()

    context = {
        'person_list': person_list,
        'youtube_list': youtube_list,
        'crew_list': crew_list,
        'poster': poster,
        'film_photo_list': film_photo_list

    }

    return render(request, 'casting/index.html', context)


def casting(request):
    ImageFormSet = modelformset_factory(PersonPhoto,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PersonPhoto.objects.none())
        print(person_form.is_valid())
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
            person.save()

            # for form in formset.cleaned_data:
            #     image = form['image']
            #     photo = Images(person=person_form, image=image)
            #     photo.save()
            # images = Images()
            #
            # images.save()
    return HttpResponse()


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['subscribe-email']
        print('here')

        email_title = 'Title'
        context = {}
        email_message = render_to_string('casting/email_subscribe.html', context)
        to_email = '{}'.format(email)

        if settings.EMAIL_FAKE == 'yes':
            print(email_message)
        else:
            email_sending = EmailMessage(email_title, email_message,
                                         to=[to_email])
            email_sending.send()
    return HttpResponse()


def person_list(request):
    if request.method == 'GET':
        person_id = request.GET.get('person_id', None)
        person = Person.objects.filter(id=person_id).get()
        contact_image = 'photos/noimage.png'
        data = {
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
            'video_url': person.video_url
        }
        return JsonResponse(data)
