from django.urls import path

from . import views
app_name = 'avi_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('edit_courses/', views.edit_courses, name='edit_courses'),
    path('delete_courses/', views.delete_courses, name='delete_courses'),
    #path(r'^edit_courses/(?P<course_code>[\w-]+)/edit/$', views.edit_courses, name='edit_courses'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('account_settings/', views.account_settings, name='account_settings'),
]
