from django.db import models

levels = [
    ('select level', 'SELECT LEVEL'),
    ('yos1', 'YOS1'),
    ('yos2', 'YOS2'),
    ('yos3', 'YOS3'),
    ('honours', 'HONOURS'),
    ('masters', 'MASTERS'),
]

class Student(models.Model):
    student_id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20, default="")
    student_current_level = models.CharField(max_length=20, choices=levels, default='select level')

    def __str__(self):
        return self.student_name + ' ' + self.student_surname + ' - ' + self.student_current_level




class Course(models.Model):
    course_code = models.CharField(max_length=8, primary_key = True)
    course_description = models.CharField(max_length=100)

    def __str__(self):  
        return self.course_code


class Enrolment(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    course_mark = models.DecimalField(decimal_places = 2, max_digits = 4)


    def __str__(self):
        return self.course_code, self.course_mark

class Predicted(models.Model):
    student_id  = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    predicted_mark = models.DecimalField(decimal_places = 2, max_digits = 4)

