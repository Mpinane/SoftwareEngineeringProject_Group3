from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create_account/', views.create_account, name='create_account'),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('edit_courses/', views.edit_courses, name='edit_courses'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('account_settings/', views.account_settings, name='account_settings'),
]