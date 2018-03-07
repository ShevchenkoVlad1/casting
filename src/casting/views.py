from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from casting.models import Person


def home(request):
    person_list = Person.objects.filter(is_main=1).order_by('-created_date')

    context = {
        'person_list': person_list
    }

    return render(request, 'casting/index.html', context)


def casting(request):
    if request.method == 'POST':
        body = {}
        for key, value in request.POST.items():
            body.update({key: value})
        person = Person()
        person.first_name = body['first_name']
        person.second_name = body['second_name']
        person.email = body['email']
        person.phone = body['phone']
        person.age = body['age']
        person.city = body['city']
        person.gender = body['gender']
        person.prof = body['prof']
        if 'experience' in body:
            person.experience = body['experience']
        if 'crowd_scene' in body:
            person.crowd_scene = True
        if 'grouping' in body:
            person.grouping = True
        if 'about_info' in body:
            person.about_info = body['about_info']
        if 'contact_image' in body:
            person.contact_image = body['contact_image']
        person.video_url = body['video_url']
        person.save()
    return HttpResponse()


def person_list(request):
    if request.method == 'GET':
        person_id = request.GET.get('person_id', None)
        person = Person.objects.filter(id=person_id).get()
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
            # 'contact_image': person.contact_image,
            'video_url': person.video_url
        }
        return JsonResponse(data)
