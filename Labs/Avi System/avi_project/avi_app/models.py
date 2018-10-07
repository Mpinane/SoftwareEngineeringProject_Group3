from django.db import models


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_password = models.CharField(max_length=20)
    student_current_level = models.CharField(max_length=20)

    @property
    def student_id_saved(self):
        return self.student_id > 0

    @property
    def student_id_not_saved(self):
        return self.student_id < 0

    @property
    def student_name_saved(self):
        return len(self.student_name) > 0

    @property
    def student_name_not_saved(self):
        return len(self.student_name) < 0

    @property
    def student_surname_saved(self):
        return len(self.student_surname) > 0

    @property
    def student_surname_not_saved(self):
        return len(self.student_surname) < 0

    @property
    def student_password_saved(self):
        return len(self.student_password) > 0

    @property
    def student_password_not_saved(self):
        return len(self.student_password) < 0

    @property
    def student_level_saved(self):
        return len(self.student_current_level) > 0

    @property
    def student_level_not_saved(self):
        return len(self.student_current_level) < 0


class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_description = models.CharField(max_length=100)

    @property
    def course_code_saved(self):
        return len(self.course_code) > 0

    @property
    def course_code_not_saved(self):
        return len(self.course_code) < 0

    @property
    def course_desc_saved(self):
        return len(self.course_description) > 0

    @property
    def course_desc_not_saved(self):
        return len(self.course_description) < 0


class Enrolment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_mark = models.DecimalField(decimal_places=2, max_digits=4)

    # student_id and course_id are Foreign Keys and have already been tested in their respective classes
    @property
    def course_mark_is_saved(self):
        return self.course_mark > 0

    @property
    def course_mark_is_not_saved(self):
        return self.course_mark < 0


class Predicted(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    predicted_mark = models.CharField(max_length=1)

    # student_id and course_code are Foreign Keys and have already been tested in their respective classes
    @property
    def predicted_mark_is_saved(self):
        return len(self.predicted_mark) > 0

    @property
    def predicted_mark_is_not_saved(self):
        return len(self.predicted_mark) < 0
