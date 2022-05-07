from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from django.db.models import Sum
from django.db.models.signals import post_save


class UpVoteManager(models.Manager):
    use_for_related_fields = True

    def upvotes(self):
        return self.get_queryset().filter(vote__gt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

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
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"comment by {self.author}"




def on_comment_saved(sender, instance, **kwargs):
    print('comment created bruh')
    print(instance)


post_save.connect(on_comment_saved, sender=Comment)
