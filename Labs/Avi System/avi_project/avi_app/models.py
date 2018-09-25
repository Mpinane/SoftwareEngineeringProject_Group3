from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(PrimaryKey = true)
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_password = models.CharField(max_length=20)
    student_current_level = models.CharField(max_length=20)

class Course(models.Model):
    course_code = models.CharField(max_length=8, PrimaryKey = true)
    course_description = = models.CharField(max_length=100)

class Enrolment(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.RESTRICT, PrimaryKey = true)
    course_id = models.ForeignKey(Course, on_delete = models.RESTRICT, PrimaryKey = true)
    course_mark = models.DecimalField()

class Predicted(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.RESTRICT, PrimaryKey = true)
    course_code = models.ForeignKey(Course, on_delete = models.RESTRICT, PrimaryKey = true)
    predicted_mark = models.DecimalField()

