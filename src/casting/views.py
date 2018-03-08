from django.forms import modelformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from casting.forms import PersonForm, ImageForm
from casting.models import Person, Image


def home(request):
    person_list = Person.objects.filter(is_main=1).order_by('-created_date')
    context = {
        'person_list': person_list,
    }

    return render(request, 'casting/index.html', context)


def casting(request):
    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
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
