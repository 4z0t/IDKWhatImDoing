from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('start/', views.start, name='start-page'),
    path('about/', views.about, name='about-page'),
    path('register/', views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout-page'),

]
