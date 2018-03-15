from django.conf import settings
from django.core.mail import EmailMessage
from django.forms import modelformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.translation import get_language
from django.views.decorators.http import require_POST, require_GET

from casting.forms import PersonForm, ImageForm
from casting.models import Person, PersonPhoto, YoutubeVideo, Worker, \
    Film_about, FilmPhoto, Partner, Social


def home(request):
    current_lang = get_language()

    person_list = Person.objects.filter(is_main=1).order_by('-created_date')
    youtube_list = YoutubeVideo.objects.all()

    crew_list = Worker.objects.filter(languages=current_lang)
    main_in_crew = crew_list.filter(is_main=1)
    crew = crew_list.filter(is_main=0)

    film_about = Film_about.objects.filter(languages=current_lang).order_by(
        '-id')[:1]
    film_photo_list = FilmPhoto.objects.all()
    partner_list = Partner.objects.all()
    # social
    twitter = Social.objects.filter(title="Twitter").get()
    instagram = Social.objects.filter(title="Instagram").get()
    youtube = Social.objects.filter(title="YouTube").get()
    facebook = Social.objects.filter(title="Facebook").get()

    context = {
        'person_list': person_list,
        'youtube_list': youtube_list,
        'main_in_crew': main_in_crew,
        'crew': crew,
        'film_about': film_about,
        'film_photo_list': film_photo_list,
        'twitter': twitter,
        'instagram': instagram,
        'youtube': youtube,
        'facebook': facebook,
        'partner_list': partner_list,
    }

    return render(request, 'casting/index.html', context)


@require_POST
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


@require_POST
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['subscribe-email']

        email_title = 'Title'
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
            'video_url': person.video_url
        }
        return JsonResponse(data)
