from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.TodoCreateView.as_view(), name='todo'), 
    path('todo/update/<int:pk>', views.TodoDetailView.as_view(), name='todo-details'), 
]
