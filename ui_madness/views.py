import json

from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import UpVote, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request: HttpRequest):
    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('comment')
            Comment.objects.create(author=request.user, content=content)
            print(f'comment added by {request.user}')
        else:
            return redirect('login-page')
    context = {
        "comments": Comment.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Now you can log in!')
            return redirect('login-page')
        else:
            messages.warning(request, 'Invalid password!')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login(request: HttpRequest):
    return render(request, 'login.html')


def start(request):
    return render(request, 'start.html')


@login_required
def profile(request: HttpRequest):
    return render(request, 'profile.html')
