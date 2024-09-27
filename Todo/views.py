from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Create your views here.

class TodoPagination(PageNumberPagination):
    page_size = 10  # Set the page size here
    page_size_query_param = 'page_size'

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
    

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [] # I don't have authentication system