import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .tasks import generate_random_number

class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'random_number_group'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        if message == 'generate':
            # Trigger Celery task
            generate_random_number.delay(self.channel_name)

    async def send_random_number(self, event):
        number = event['number']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'number': number
        })) 