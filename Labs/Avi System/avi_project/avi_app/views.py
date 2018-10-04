from avi_app.models import Student, Course, Enrolment, Predicted

from django.shortcuts import render

from django.shortcuts import redirect

import course_recommender

#from django.utils import simplejson
from django.http import HttpResponseRedirect
from .forms import CreateAccountForm
from .forms import LoginForm
from .forms import AddCourseForm

from .models import Student


def create_account(request):
    form = CreateAccountForm(request.POST)
    context = {
        'form': form
    }

    if(request.method == 'POST'):
        
        if(form.is_valid()):
            student_id = request.POST.get("student_id")
            student_name = request.POST.get("student_name")
            student_surname = request.POST.get("student_surname")
            student_password = request.POST.get("student_password")
            student_current_level = request.POST.get("student_current_level")
            Student.objects.create(student_id = student_id, 
                                student_name = student_name,
                                student_surname =  student_surname,
                                student_password = student_password,
                                student_current_level = student_current_level)
            return redirect('login')
    else:
            form = CreateAccountForm()
    
    return render(request,'avi_app/create_account.html',context)


def login(request):
    form = LoginForm(request.POST)
    context = {
        'form': form
    }

    if(request.method == 'POST'):
        
        if(form.is_valid()):
            student_id = request.POST.get("student_id")
            student_password = request.POST.get("student_password")
            try:
                student = Student.objects.get(student_id=student_id, student_password=student_password )
                request.session['id'] = student_id
                return redirect('home')
            except Student.DoesNotExist:
               return redirect('login')

    return render(request,'avi_app/login.html',context)



def home(request):
    ''' student_id = request.session.get('id')
    request.session['id'] = student_id'''
    return render(request,'avi_app/home.html')

def courses(request):
    form = AddCourseForm(request.POST)
    context = {
        'enrolment': Enrolment.objects.filter(student_id=request.session.get('id')),
        'form': form
    }

    if(request.method == 'POST'):
        
        # if(form.is_valid()):
        courses= request.POST.get("course_id")
        student_id = Student.objects.get(student_id=request.session.get('id'))
        course_id = Course.objects.get(course_code=request.POST.get("course_id"))
        course_mark = request.POST.get("course_mark")
        Enrolment.objects.create(student_id = student_id, 
                            course_id = course_id,
                            course_mark =  course_mark,)
        return redirect('courses')
    else:
            form = CreateAccountForm()

    return render(request,'avi_app/courses.html',context)

def edit_courses(request):
    context = {
        'enrolment': Enrolment.objects.filter(student_id=request.session.get('id')),
    }

    if(request.method == 'POST'):
        
        for e in Enrolment.objects.filter(student_id=request.session.get('id')):
            course_mark = request.POST.get(str(e.id) + "_grade")
            e.course_mark = course_mark
            e.save()
        return redirect('courses')

    return render(request,'avi_app/edit_courses.html',context)

def recommendations(request):
    enrol =  Enrolment.objects.filter(student_id=request.session.get('id'))
    highest_level = Student.objects.get(student_id=request.session.get('id')).student_current_level
    course_and_mark=[]
    course_and_mark.append([])
    course_and_mark.append([])

    for e in enrol:
        course_and_mark[0].append(e.course_id.course_code)
        course_and_mark[1].append(e.course_mark)

    if(request.method == 'POST'):
        course_recommender.recommend_course(enrol,highest_level)
        predicted = course_recommender.predict()
        student_id = Student.objects.get(student_id=request.session.get('id'))

        for i in range(len(predicted[0])):
            course_id = Course.objects.get(course_code=predicted[0][i])
            course_mark = predicted[1][i]
            Predicted.objects.create(student_id = student_id, 
                            course_id = course_id,
                            course_mark =  course_mark,)

        return redirect('recommendations')
        
    context = {
        'nums': [1,2,3,4,5,6,7,8,9,10],
        'predict': Predicted.objects.filter(student_id=request.session.get('id')),
    }
    return render(request,'avi_app/recommendations.html',context)

def account_settings(request):
    context = {
        'first': "Mpinane",
        'surname': "Mohale",
        'student_number': "1363679"
    }
    return render(request,'avi_app/account_settings.html',context)

def delete(request,id):
    #return render(request,'avi_app/account_settings.html',context)
    Enrolment.objects.get(id=id).delete()
    return redirect('courses')