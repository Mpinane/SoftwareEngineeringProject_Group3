from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Course
from .models import Enrolment
from .models import Predicted

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrolment)
admin.site.register(Predicted)