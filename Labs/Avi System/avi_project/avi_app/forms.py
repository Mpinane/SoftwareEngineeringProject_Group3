from django import forms
from avi_app.models import Course

LEVEL_OF_STUDY =  [
    ('-1', 'Current Level of Study'),
    ('yos1', 'YOS1'),
    ('yos2', 'YOS2'),
    ('yos3', 'YOS3'),
    ('honours', 'Honours'),
    ('masters', 'Masters'),
    ]

class CreateAccountForm(forms.Form):
    student_id = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Student Number'}))
    student_name = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'placeholder': 'Student Firstname'}))
    student_surname = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'placeholder': 'Student Surname'}))
    student_password = forms.CharField(max_length=20, 
                        widget = forms.PasswordInput(attrs={'placeholder': 'Student Password'}))
    confirm_password = forms.CharField(max_length=20, 
                        widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    student_current_level = forms.CharField(max_length=20,
                            widget=forms.Select(choices = LEVEL_OF_STUDY))

class LoginForm(forms.Form):
    student_id = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Student Number'}))
    student_password = forms.CharField(max_length=20, 
                        widget = forms.PasswordInput(attrs={'placeholder': 'Student Password'}))

class AddCourseForm(forms.Form):
    #student_id  = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Student Number'}))
    course_id = forms.CharField(max_length=8, widget = forms.TextInput(attrs={'placeholder': 'Course Code'}))
    course_mark = forms.DecimalField(decimal_places = 2, max_digits = 4, widget = forms.NumberInput(attrs={'placeholder': 'percentage(%)'}))
    