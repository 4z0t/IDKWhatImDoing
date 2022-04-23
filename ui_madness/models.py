from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from django.db.models import Sum
 
class UpVoteManager(models.Manager):
 
    use_for_related_fields = True
 
    def upvotes(self):
        return self.get_queryset().filter(vote__gt=0)
 
    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def articles(self):
        return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')
 
    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')


class UpVote(models.Model):
  

    UPVOTED = 1
    NOTUPVOTED = 0
 
    VOTES = (
        (NOTUPVOTED, 'not upvoted'),
        (UPVOTED, 'upvoted')
    )
 
    vote = models.SmallIntegerField(verbose_name="vote", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)
 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = UpVoteManager()

 
 
class Article(models.Model):
    votes = GenericRelation(UpVote, related_query_name='articles')
    text = models.TextField(max_length=100)
 
 
class Comment(models.Model):
    votes = GenericRelation(UpVote, related_query_name='comments')