from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('', views.create_account, name='create_account'),
    path('', views.home, name='home'),
    path('', views.courses, name='courses'),
    path('', views.recommendations, name='recommendations'),
    path('', views.account_settings, name='account_settings'),
]