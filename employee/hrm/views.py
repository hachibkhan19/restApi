from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.
class homeView(View):
    def get(self, request):
        return HttpResponse('hi')
