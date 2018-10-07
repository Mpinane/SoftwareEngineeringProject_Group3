from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest


class TestUrls:  # Tests URLS
    # Tests home url successful redirect
    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    # Counter Test
    def test_not_home_url(self):
        path = reverse('account_settings')
        assert resolve(path).view_name != 'home'

    # Tests Login url successful redirect
    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    # Counter Test
    def test_not_login_url(self):
        path = reverse('create_account')
        assert resolve(path) != 'login'

    # Tests create account url successful redirect
    def test_create_account_url(self):
        path = reverse('create_account')
        assert resolve(path) == 'create_account'

    # Counter Test
    def test_not_create_account_url(self):
        path = reverse('login')
        assert resolve(path) != 'create_account'

    # Tests account settings url successful redirect
    def test_account_settings_url(self):
        path = reverse('account_settings')
        assert resolve(path).view_name == 'account_settings'

    # Counter Test
    def test_not_account_settings_url(self):
        path = reverse('home')
        assert resolve(path).view_name != 'account_settings'

    # Tests courses url successful redirect
    def test_courses(self):
        path = reverse('courses')
        assert resolve(path).view_name == 'courses'

    # Counter Test
    def test_not_courses(self):
        path = reverse('edit_courses')
        assert resolve(path).view_name != 'courses'

    # Tests Edit Courses url successful redirect
    def test_edit_courses(self):
        path = reverse('edit_courses')
        assert resolve(path).view_name == 'edit_courses'

    # Counter Test
    def test_not_edit_courses(self):
        path = reverse('courses')
        assert resolve(path).view_name != 'edit_courses'

    # Tests auto redirect on startup url successful redirect
    def test_auto_login_page_redirect(self):
        path = reverse('')
        assert resolve(path).view_name == 'login'

    # Counter Test
    def test_not_auto_login_page_redirect(self):
        path = reverse('home')
        assert resolve(path).view_name != 'login'

    # Tests delete url successful current poage redirect
    def test_delete_url(self):
        path = reverse('delete/1')
        assert resolve(path).view_name == 'delete'

    # Counter Test
    def test_not_delete_url(self):
        path = reverse('edit_courses')
        assert resolve(path).view_name != 'delete'


@pytest.mark.django_db
class TestModels:
    # Differs from Tests.py Model tests in that it doesnt check for created objects, rather individual database entries-
    # using the mixer blend function

    # STUDENT MODEL TESTS

    # Tests whether student_id stored in database
    def test_id_is_stored(self):
        student = mixer.blend('avi_app.Student', student_id=100000)
        assert student.student_id_saved == True

    # Counter Test
    def test_id_is_not_stored(self):
        student = mixer.blend('avi_app.Student', student_id=100000)
        assert student.student_id_not_saved == False

    # Tests whether student_name stored in database
    def test_name_is_stored(self):
        student = mixer.blend('avi_app.Student', student_name="Frank")
        assert student.student_name_saved == True

    # Counter Test
    def test_name_is_not_stored(self):
        student = mixer.blend('avi_app.Student', student_name="Frank")
        assert student.student_name_not_saved == False

    # Tests whether student_surname stored in database
    def test_surname_is_stored(self):
        student = mixer.blend('avi_app.Student', student_suname="Johnson")
        assert student.student_surname_saved == True

    # Counter Test
    def test_surname_is_not_stored(self):
        student = mixer.blend('avi_app.Student', student_suname="Johnson")
        assert student.student_surname_not_saved == False

    # Tests whether student_password stored in database
    def test_password_is_stored(self):
        student = mixer.blend('avi_app.Student', student_password="pass1234")
        assert student.student_password_saved == True

    # Counter Test
    def test_password_is_not_stored(self):
        student = mixer.blend('avi_app.Student', student_password="pass1234")
        assert student.student_password_not_saved == False

    # Tests whether student_current_level stored in database
    def test_level_is_stored(self):
        student = mixer.blend('avi_app.Student', student_current_level=3)
        assert student.student_level_saved == True

    # Counter Test
    def test_level_is_not_stored(self):
        student = mixer.blend('avi_app.Student', student_current_level=3)
        assert student.student_level_not_saved == False


    # COURSE MODEL

    # Tests whether course_code stored in database
    def test_course_is_stored(self):
        course = mixer.blend('avi_app.Course', course_code="COMS1018")
        assert course.course_code_saved == True

    # Counter Test
    def test_course_is_not_stored(self):
        course = mixer.blend('avi_app.Course', course_code="COMS1018")
        assert course.course_code_saved == True

    # Tests whether course_desc stored in database
    def test_course_desc_is_stored(self):
        course = mixer.blend('avi_app.Course', course_description="Programming Intro")
        assert course.course_desc_saved == True

    # Counter Test
    def test_course_desc_is_not_stored(self):
        course = mixer.blend('avi_app.Course', course_description="Programming Intro")
        assert course.course_desc_saved == True

    # ENROLMENT MODEL
    # Tests whether enrolment course_mark stored in database
    def test_enrolment_course_mark_is_stored(self):
        enrol = mixer.blend('avi_app.Enrolment', course_mark=80)
        assert enrol.course_mark_is_saved == True

    # Counter Test
    def test_enrolment_course_mark_is_not_stored(self):
        enrol = mixer.blend('avi_app.Enrolment', course_mark=80)
        assert enrol.course_mark_is_saved == True

    # PREDICTED MODEL
    # Tests whether Predicted Table mark stored in database
    def test_predicted_mark_is_stored(self):
        p = mixer.blend('avi_app.Predicted', predicted_mark=80)
        assert p.predicted_mark_is_saved == True

    # Counter Test
    def test_predicted_mark_is_not_stored(self):
        p = mixer.blend('avi_app.Predicted', predicted_mark=80)
        assert p.predicted_mark_is_saved == True
