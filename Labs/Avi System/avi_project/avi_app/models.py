from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_password = models.CharField(max_length=20)
    student_current_level = models.CharField(max_length=20)

class Course(models.Model):
    course_code = models.CharField(max_length=8, primary_key = True)
    course_description = models.CharField(max_length=100)

class Enrolment(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    course_mark = models.DecimalField(decimal_places = 2, max_digits = 4)

class Predicted(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    predicted_mark = models.DecimalField(decimal_places = 2, max_digits = 4)

