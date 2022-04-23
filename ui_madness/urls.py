from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('login/', views.login, name='login-page'),
    path('start/', views.start, name='start-page'),
    path('loginvalidate/', views.login_validate, name='login'),
  
]
