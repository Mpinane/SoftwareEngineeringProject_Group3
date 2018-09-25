from django.shortcuts import render

from django.http import HttpResponse

#from .models import Student


def login(request):
    return render(request,'avi_app/login.html')

def create_account(request):
    return render(request,'avi_app/create_account.html')

def home(request):
    return render(request,'avi_app/home.html')

def courses(request):
    return render(request,'avi_app/courses.html')

def recommendations(request):
    return render(request,'avi_app/recommendations.html')

def account_settings(request):
    return render(request,'avi_app/account_settings.html')
