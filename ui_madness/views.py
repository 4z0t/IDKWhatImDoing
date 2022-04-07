from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    context = {
        "current_time": datetime.now().strftime("%H:%M:%S")
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')

def start(request):
    return render(request, 'start.html')