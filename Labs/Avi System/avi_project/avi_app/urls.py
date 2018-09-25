from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('home/', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('account_settings', views.account_settings, name='account_settings'),
]