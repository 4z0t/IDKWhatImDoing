from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .comment_updater import CommentUpdateConsumer
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('start/', views.start, name='start-page'),
    path('about/', views.about, name='about-page'),
    path('register/', views.register, name='register-page'),
    path('profile/', views.profile, name='profile-page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout-page'),
]

websockets = AuthMiddlewareStack(
    URLRouter(
        [path('comment/', CommentUpdateConsumer.as_asgi(), name='comment-update')]
    )
)
