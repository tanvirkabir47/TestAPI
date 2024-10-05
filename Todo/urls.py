from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoCreateView.as_view(), name='todo'), 
    path('todo/get/<int:pk>', views.TodoView.as_view(), name='todo-details'), 
    path('todo/update/<int:pk>', views.TodoUpdateView.as_view(), name='todou'), 
    path('todo/delete/<int:pk>', views.TodoDeleteView.as_view(), name='todod'), 
]
