from django.shortcuts import render
import json
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpRequest
from django.views import View
from Bot import Bot
from django.contrib.contenttypes.models import ContentType
from .models import UpVote, Article


dummy_articles = [
  {
  "type":"article",
    "data":Article(text="""
                   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
    
    }
]
 

def home(request):
    context = {
        "articles": dummy_articles
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
    Bot.senddata(data)
    return render(request, 'start.html')




 
 
class UpVotesView(View):
    model = None    # Модель данных - Статьи или Комментарии
    vote_type = None # Тип комментария 
 
    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        try:
            upvote = UpVote.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
            if upvote.vote is not self.vote_type:
                upvote.vote = self.vote_type
                upvote.save(update_fields=['vote'])
                result = True
            else:
                upvote.delete()
                result = False
        except UpVote.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True
 
        return HttpResponse(
            json.dumps({
                "result": result,
                "upvotes_count": obj.votes.upvotes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )