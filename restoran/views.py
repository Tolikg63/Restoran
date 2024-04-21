from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


class BaseIndex(View):
    def get(self, request):
        return render(request, 'restoran/index.html')