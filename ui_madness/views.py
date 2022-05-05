from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpRequest
from django.views import View
from Bot import Bot
from django.contrib.contenttypes.models import ContentType
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
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            print('user registered')
            return redirect('home-page')
        else:
            print('invalid')
    else:
        form = UserCreationForm()

    return render(request, 'login.html', {'form': form})


def start(request):
    return render(request, 'start.html')


def login_validate(request: HttpRequest):
    data = request.body
    data = json.loads(data)
    Bot.senddata(data)
    return render(request, 'start.html')

# class UpVotesView(View):
#     model = None    # Модель данных - Статьи или Комментарии
#     vote_type = None # Тип комментария
#
#     def post(self, request, pk):
#         obj = self.model.objects.get(pk=pk)
#         try:
#             upvote = UpVote.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
#             if upvote.vote is not self.vote_type:
#                 upvote.vote = self.vote_type
#                 upvote.save(update_fields=['vote'])
#                 result = True
#             else:
#                 upvote.delete()
#                 result = False
#         except UpVote.DoesNotExist:
#             obj.votes.create(user=request.user, vote=self.vote_type)
#             result = True
#
#         return HttpResponse(
#             json.dumps({
#                 "result": result,
#                 "upvotes_count": obj.votes.upvotes().count(),
#                 "sum_rating": obj.votes.sum_rating()
#             }),
#             content_type="application/json"
#         )
