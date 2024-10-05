import json
from channels.generic.websocket import WebsocketConsumer
from django.utils.timezone import now  # To handle `created_at`

class TodoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("WebSocket connected")  # Debug message for connection

    def disconnect(self, close_code):
        print(f"WebSocket disconnected: {close_code}") 

    def receive(self, text_data):
        from .models import Todo  

        try:
            text_data_json = json.loads(text_data)
            action = text_data_json.get('action', None)

            if action == 'list':
                # List all todos
                todos = Todo.objects.all().values('id', 'title', 'description', 'completed')
                todo_list = list(todos)  # Convert queryset to list of dictionaries

                self.send(text_data=json.dumps({
                    'todos': todo_list
                }))

            elif action == 'create':
                # Create a new todo item
                title = text_data_json.get('title', None)
                description = text_data_json.get('description', '')

                if title:
                    new_todo = Todo.objects.create(
                        title=title,
                        description=description,
                        created_at=now(),
                        completed=False
                    )

                    # Send success response with the new todo item details
                    self.send(text_data=json.dumps({
                        'message': 'Todo created successfully',
                        'todo': {
                            'id': new_todo.id,
                            'title': new_todo.title,
                            'description': new_todo.description,
                            'completed': new_todo.completed
                        }
                    }))

                else:
                    # Send an error response if title is missing
                    self.send(text_data=json.dumps({
                        'error': 'Title is required to create a Todo'
                    }))
                    print("Failed to create Todo: Title is missing")

        except Exception as e:
            print(f"Error processing message: {str(e)}")
            self.send(text_data=json.dumps({
                'error': f'Error: {str(e)}'
            }))