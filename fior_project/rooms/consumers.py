import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Msg, Room
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        msg = text_data_json['msg']
        username = text_data_json['username']
        room = text_data_json['room']

        await self.save_msg(username, room, msg)

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type' : 'send_msg',
                'msg' : msg,
                'username' : username,
                'room' : room
            })

    async def send_msg(self, event):
        msg = event['msg']
        username = event['username']
        room = event['room']

        await self.send(text_data = json.dumps({'msg' : msg, 'username' : username, 'room' : room}))

    @sync_to_async
    def save_msg(self, username, room, msg):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Msg.objects.create(user=user, room=room, content=msg)