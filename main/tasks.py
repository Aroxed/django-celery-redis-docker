import random
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def generate_random_number(channel_name):
    # Generate random number
    number = random.randint(1, 100)
    
    # Get channel layer
    channel_layer = get_channel_layer()
    
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(
        channel_name,
        {
            'type': 'send_random_number',
            'number': number
        }
    )
    
    return number 