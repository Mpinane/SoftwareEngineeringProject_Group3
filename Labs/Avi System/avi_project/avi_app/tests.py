from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse
from .models import Enrolment
from .models import Predicted
from .models import Student
from .models import Course

# It’s always a good idea to test both expected and unexpected behavior .
# These are Commented as Test and Counter Test.
# It is essential that both instances are considered whether they seem trivial or not.
# This is how our tests are conducted.

# run 'python manage.py test' to show number of test cases passed, failed


class HomePageTests(SimpleTestCase):  # Tests Home Page Redirect
    # Tests Home Page Success Status Code.
    def test_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    # Counter Test.
    def test_not_home(self):
        response = self.client.get('not_home')
        self.assertEquals(response.status_code, 404)

    # Tests whether correct html page loads.
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    # Counter Test.
    def test_not_view_url_by_name(self):
        response = self.client.get(reverse('not_home'))
        self.assertNotEquals(response.status_code, 200)

    # Tests whether correct Template is used.
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # Counter Test.
    def test_view_doesnt_use_correct_template(self):
        response = self.client.get(reverse('invalid'))
        self.assertNotEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'home.html')

    # Tests whether home page html correct.
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home')

    # Counter Test.
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('home')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertContains(response, 'Courses')
        self.assertContains(response, 'marks')
        self.assertNotContains(response, 'add')
        self.assertContains(response, 'Account Settings')


class LoginPageTests(SimpleTestCase):  # login page tests
    # Tests Login Page Success Status Code.
    def test_login_page_status_code(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    # Counter Test
    def test_not_login_page_status_code(self):
        response = self.client.get('/not_login/')
        self.assertEquals(response.status_code, 404)

    # Tests whether correct html page loads.
    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    # Counter Test
    def test_not_view_url_by_name(self):
        response = self.client.get(reverse('not_login'))
        self.assertNotEquals(response.status_code, 200)

    # Tests whether correct template is used
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    # Counter Test
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'login.html')

    # Tests correct html loaded
    def test_login_page_contains_correct_html(self):
        response = self.client.get('/login/')
        self.assertContains(response, '<h3>Login</h3>')

    # Counter Test
    def test_login_page_doesnt_contains_correct_html(self):
        response = self.client.get('/login/')
        self.assertNotContains(response, '<h3>Signout</h3>')

    # Tests that no incorrect html content on html file
    def test_login_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertNotContains(response, 'courses')
        self.assertNotContains(response, 'marks')
        self.assertNotContains(response, 'add')
        self.assertNotContains(response, 'settings')


class StudentTests(TestCase):  # Tests Database Usage
    # create new Student Object
    def setUp(self, x):
        Student.objects.create(100000, "john", "Smith", "js123", 3)
        return Student.objects.get(id=x)

    # Tests whether student_id is stored in database
    def test_student_id(self):
        student = StudentTests.setUp(self, 1)
        expected_student_id = f'{student.student_id}'
        self.assertEquals(expected_student_id, 100000)

    # Tests whether student_name is stored in database
    def test_name(self):
        student = Student.objects.get(id=1)
        expected_student_name = f'{student.student_name}'
        self.assertEquals(expected_student_name, 'john')

    # Tests whether student_surname is stored in database
    def test_surname(self):
        student = Student.objects.get(id=1)
        expected_student_surname = f'{student.student_name}'
        self.assertEquals(expected_student_surname, 'john')

    # Tests whether student_current_level is stored in database
    def test_current_year(self):
        student = Student.objects.get(id=1)
        expected_current_year = f'{course.student_current_level}'
        self.assertNotEquals(expected_current_year, 1)
        self.assertNotEquals(expected_current_year, 1)
        self.assertEquals(expected_current_year, 3)

    # Tests whether correct view is loaded
    def test_view(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'just a test')
        self.assertTemplateUsed(response, 'courses.html')


class CoursesTests(TestCase):
    # Creates a Courses Object
    def setUp(self, x):
        Course.objects.create("COMS1000", "Computer Hardware Intro")
        return Course.objects.get(id=x)

    # Tests whether course_code is stored in database
    def test_course_code(self):
        course = CoursesTests.setUp(self, 1)
        expected_course_code = course.course_code
        self.assertEquals(expected_course_code, "COMS1000")

    # Tests whether course description is stored in database
    def test_desc(self):
        course = CoursesTests.setUp(self, 1)
        expected_course_desc = course.course_description
        self.assertEquals(expected_course_desc, "Computer Hardware Intro")

    # Tests whether correct view loaded
    def test_view(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'just a test')
        self.assertTemplateUsed(response, 'courses.html')


class EnrolmentTests(TestCase):
    # Creates new Enrolment Object
    def setUp(self, x):
        Enrolment.objects.create(100000, "COMS1000", 88)
        return Enrolment.objects.get(id=x)

    # Tests whether Enrolment student_id is stored in database
    def test_enrol_student_id(self):
        enrolment = EnrolmentTests.SetUp(self, 1)
        expected_student_id = enrolment.student_id
        self.assertEquals(expected_student_id, 10000)
        self.assertNotEquals(expected_student_id, 999999)

    # Tests whether Enrolmnt course_code is stored in database
    def test_enrol_course_code(self):
        enrolment = EnrolmentTests.SetUp(self,1)
        expected_course_code = enrolment.course_id
        self.assertEquals(expected_course_code, "COMS1000")
        self.assertNotEquals(expected_course_code, "COMS4000")


class PredictedTests(TestCase):
    # Creates new Predicted Object
    def setUp(self, x):
        Predicted.objects.create(10000, "COMS4001", 80)
        return Predicted.objects.get(id=x)

    # Tests whether Predicted object is valid
    def test_valid(self):
        valid = PredictedTests.setUp(self, 1)
        self.assertTrue(valid, Predicted.objects.exists())

    # Tests whether Predicted Table student_id is stored in database
    def test_student_id_predicted(self):
        predicted = PredictedTests.setUp(self, 1)
        expected_student_id = predicted.student_id
        self.assertEquals(expected_student_id, 10000)
        self.assertNotEquals(expected_student_id, 4000000)

    # Tests whether Predicted Table course_code is stored in database
    def test_course_code_predicted(self):
        predicted = PredictedTests.setUp(self, 1)
        expected_course_code = predicted.course_code
        self.assertEquals(expected_course_code, "COMS4001")
        self.assertNotEquals(expected_course_code, "COMS1000")

    # Tests whether Predicted Table predicted_mark is stored in database
    def test_predicted_mark(self):
        predicted = PredictedTests.setUp(self, 1)
        expected_predicted_mark = predicted.predicted_mark
        self.assertEquals(expected_predicted_mark, 80)
        self.assertNotEquals(expected_predicted_mark, 100)
        self.assertNotEquals(expected_predicted_mark, 50)