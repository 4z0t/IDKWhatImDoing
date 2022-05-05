from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import UpVote, Comment
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages



def home(request):
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
            messages.success(request, f'Account created for {username}')
            print('user registered')
            return redirect('home-page')
        else:
            messages.warning(request, 'Invalid password!')
            print('invalid')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login(request: HttpRequest):
    return render(request, 'login.html')


def start(request):
    return render(request, 'start.html')
