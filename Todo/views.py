from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo
from django.db.models import Q

# Create your views here.


class TodoCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [] # I don't have authentication system
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        search = self.request.GET.get('search', None)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        return queryset
    

class TodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [] # I don't have authentication system
    
    
class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [] # I don't have authentication system
    
    
class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [] # I don't have authentication system