import json

from channels.exceptions import DenyConnection
from channels.generic.websocket import WebsocketConsumer

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser

from .models import Comment


class CommentUpdateConsumer(WebsocketConsumer):
    _group_name = 'CommentUpdate'

    def connect(self):
        if self.scope['user'] == AnonymousUser():
            raise DenyConnection("User does not exist")
        print(f"connected {self.scope['user']}")
        self.channel_layer.group_add(
            self._group_name,
            self.channel_name
        )

        self.accept()



    def update_comment(self, comment):
        self.channel_layer.group_send(
            self._group_name,
            {
                'type': 'comment_update',
                'author': comment.author.username,
                'content': comment.content,
                'date': comment.date_commented
            }
        )

    def websocket_disconnect(self, message):
        self.channel_layer.group_discard(
            self._group_name,
            self.channel_name
        )
