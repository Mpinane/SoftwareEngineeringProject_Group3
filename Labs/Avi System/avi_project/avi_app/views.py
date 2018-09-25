from django.shortcuts import render

from django.http import HttpResponse

from .models import Student


def index(request):
    return render(request,'pols/index.html')
