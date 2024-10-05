import json
from channels.generic.websocket import WebsocketConsumer

class TodoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("WebSocket connected")  # Debug message for connection

    def disconnect(self, close_code):
        print(f"WebSocket disconnected: {close_code}")  # Debug message for disconnection

    def receive(self, text_data):
        from .models import Todo  # Move import here

        print(f"Data received: {text_data}")  # Debug message for received data
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', None)
            print(f"Message received: {message}")

            if message == 'list':
                todos = Todo.objects.all().values('id', 'title', 'description', 'completed')
                todo_list = list(todos)  # Convert queryset to list of dictionaries

                self.send(text_data=json.dumps({
                    'todos': todo_list
                }))
                print("Todo list sent")

            elif message == 'ping':
                self.send(text_data=json.dumps({
                    'message': 'pong'
                }))
                print("Sent pong message")

            else:
                self.send(text_data=json.dumps({
                    'error': 'Unknown command'
                }))
        except Exception as e:
            print(f"Error processing message: {str(e)}")