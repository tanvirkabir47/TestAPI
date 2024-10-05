import json
from channels.generic.websocket import WebsocketConsumer
from .models import Todo

class TodoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # Send a welcome message on connection
        self.send(text_data=json.dumps({
            'message': 'Connected to Todo WebSocket'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action', '')

        if action == 'create':
            self.create_todo(data)
        elif action == 'list':
            self.list_todos()
        else:
            self.send(text_data=json.dumps({
                'message': 'Unknown action'
            }))

    def create_todo(self, data):
        title = data.get('title')
        description = data.get('description', '')

        # Create the new Todo entry
        todo = Todo.objects.create(title=title, description=description)

        # Send a response back with the created todo
        self.send(text_data=json.dumps({
            'message': f'Todo "{todo.title}" created successfully!',
            'todo': {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'created_at': str(todo.created_at),
                'completed': todo.completed
            }
        }))

    def list_todos(self):
        todos = Todo.objects.all().values('id', 'title', 'description', 'created_at', 'completed')
        todos_list = list(todos)

        # Send the list of todos
        self.send(text_data=json.dumps({
            'todos': todos_list
        }))