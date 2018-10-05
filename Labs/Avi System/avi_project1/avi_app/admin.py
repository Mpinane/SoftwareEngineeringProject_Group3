from django.contrib import admin
from .models import Student, Course, Enrolment, Predicted

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrolment)
admin.site.register(Predicted)


