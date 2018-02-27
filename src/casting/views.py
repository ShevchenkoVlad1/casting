from django.shortcuts import render, redirect
from django.views.generic import View

from app.utils import body_parser


class Home(View):
    def get(self, request):
        context = {}
        return render(request, 'casting/index.html', context)

    @body_parser
    def post(self, request, data):
        pass
