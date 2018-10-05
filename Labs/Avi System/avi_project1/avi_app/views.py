from django.shortcuts import render, get_object_or_404, redirect
#from django.views.decorators.csrf import csrf_protect
from .forms import RegistrationForm, CourseForm, EnrolmentForm, PredictedForm
from django.http import HttpResponse
#from edit_courses import myform

#from django.utils import simplejson

from .models import Student, Course, Enrolment, Predicted


def login(request):
    return render(request,'avi_app/login.html')

def home(request):
    return render(request, 'avi_app/home.html')

def create_account(request):
    form = RegistrationForm()
    if request.method == 'POST':
         form = RegistrationForm(request.POST)
    if form.is_valid():
            data = form.save(commit=False)
            data.student_id = request.POST.get('student_id')
            data.student_name = request.POST.get('student_name')
            data.student_surname = request.POST.get('student_surname')
            data.student_current_level = request.POST.get('student_current_level')
            data.student_password = request.POST.get('student_password')
            data.confirm_password = request.POST.get('confirm_password')
            print(form.cleaned_data)
            form.save()
            form = RegistrationForm()
           

    context = {
        "form": form
    }
    print(request.POST)
    print(request.GET)
    return render(request,'avi_app/create_account.html', context)

def courses(request):
      eform = EnrolmentForm()
      all_courses = Enrolment.objects.all()
      if request.method == 'POST':
         eform = EnrolmentForm(request.POST)
      if eform.is_valid():
          e1 = eform.save(commit=False)

          try:
              ecourses = Course.objects.get(pk=Student.student_id)
          except Course.DoesNotExist:
              ecourses = None

          
          ecourses = Course
          c = request.POST.get('course_code')
          e1.course_code = Course.objects.get(course_code= c)
          e1.course_mark = request.POST.get('course_mark')

          print(eform.cleaned_data)
          eform.save()
          eform = EnrolmentForm()

         

      context = {
        "form": eform,
        "all_courses": all_courses
    }
      return render(request, 'avi_app/courses.html', context)


# def edit_courses(request, course_code=None):
#     instance = get_object_or_404(Enrolment, course_code = course_code)
#     form = EnrolmentForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#        # all_enrolments = Enrolment.objects.all()

#         return redirect(instance.get_absolute_url())

#     context = {
#         'course_code': instance.course_code,
#         'instance': instance,
#         'form': form,
#     }

#     return render(request, 'avi_app/edit_courses.html', context)

def edit_courses(request):
   

    all_enrolments = Enrolment.objects.all()

    context={
        'object_list': all_enrolments
    }

    return render(request, 'avi_app/edit_courses.html', context)


def delete_courses(request, course_code):
    course_instance =get_object_or_404(Enrolment, course_code =course_code)
    if request.method == 'POST':
        course_instance.delete()
        return redirect('avi_app/edit_courses.html')
    
    context = {
        'object': course_instance
    }

    return render(request, 'avi_app/delete_courses.html', context)



#def edit_courses(request):
    #if request.method == 'POST':
      
        #course = .get(c)
        #cours object.set(c)
   # all_enrolments = Enrolment.objects.all()

    #context = {
    #    'all_enrolments': all_enrolments
   # }

    #form = myform
    #changed_grade =
     #Enrolment.objects.get(course=request.GET.get['course_code'])
    #changed_course = form.c.value()
   # print(changed_course)
     #Enrolment.objects.get(course=request.GET.get['course_mark'])
    #changed_course.save()
    #changed_grade.save()

    #return render(request, 'avi_app/edit_courses.html', context)

#def edit_courses(request):
 #   return render(request,'avi_app/edit_courses.html')

 #def Save_changes(request):
    # all

def recommendations(request):
    predicted = Predicted.objects.all() 
    context = {
        'object_list': predicted
    }
    return render(request,'avi_app/recommendations.html',context)

def account_settings(request):
    context = {
        'first': "Mpinane",
        'surname': "Mohale",
        'student_number': "1363679"
    }
    return render(request,'avi_app/account_settings.html',context)
