from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpRequest
import json

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


def login_validate(request: HttpRequest):
    data = request.body
    data = json.loads(data)
    print(data)
    return render(request, 'start.html')
