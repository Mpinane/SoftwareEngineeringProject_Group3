from django.forms import ModelForm
from .models import Student, Course, Enrolment, Predicted

class RegistrationForm(ModelForm):

    class Meta:
        model = Student
        fields =[
            'student_name', 
            'student_surname',
            'student_id',
            'student_current_level',
            'student_password',
            'confirm_password'

        ]

class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields =[
            'course_code',
            'course_description'
        ]

class EnrolmentForm(ModelForm):

    class Meta:
        model = Enrolment
        fields =[
            'student_id',
            'course_code',
            'course_mark'
        ]

class PredictedForm(ModelForm):

    class Meta:
        model = Predicted
        fields = [
            'student_id',
            'course_code',
            'predicted_mark'
        ]
