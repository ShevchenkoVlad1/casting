from django import forms

from casting.models import Person, Image


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=70)
    second_name = forms.CharField(max_length=35)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    age = forms.DateField()
    city = forms.CharField(max_length=70)
    gender = forms.CharField(max_length=70)
    prof = forms.CharField(max_length=70)
    experience = forms.CharField(max_length=1000, required=False)
    grouping = forms.BooleanField()
    crowd_scene = forms.BooleanField()
    about_info = forms.CharField(max_length=1000, required=False)
    video_url = forms.CharField(max_length=70, required=False)

    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'email', 'phone', 'age',
                  'city', 'gender', 'prof', 'experience', 'grouping',
                  'crowd_scene', 'about_info', 'video_url',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Image
        fields = ('image',)
