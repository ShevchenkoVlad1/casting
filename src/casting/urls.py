from django.urls import path

from casting.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
