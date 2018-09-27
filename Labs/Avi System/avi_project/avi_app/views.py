from django.shortcuts import render

from django.http import HttpResponse

#from django.utils import simplejson

#from .models import Student


def login(request):
    return render(request,'avi_app/login.html')

def create_account(request):
    return render(request,'avi_app/create_account.html')

def home(request):
    return render(request,'avi_app/home.html')

def courses(request):
    context = {
        'nums': [1,2,3,4,5,6,7,8,9,10],
        'courses': ["COMS1100","MATH1024","INFO1000"]
    }
    return render(request,'avi_app/courses.html',context)

def edit_courses(request):
    context = {
        'nums': [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'avi_app/edit_courses.html',context)

def recommendations(request):
    context = {
        'nums': [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'avi_app/recommendations.html',context)

def account_settings(request):
    context = {
        'first': "Mpinane",
        'surname': "Mohale",
        'student_number': "1363679"
    }
    return render(request,'avi_app/account_settings.html',context)
