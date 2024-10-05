import json
from channels.generic.websocket import WebsocketConsumer

class TodoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'WebSocket connection established'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', 'No message received')
        self.send(text_data=json.dumps({
            'message': f'You sent: {message}'
        }))