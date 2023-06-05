from django.shortcuts import render
from django.http import HttpResponse
from .signals import post_request_signal

# Create your views here.
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

filter = []
number = []

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    todos = Todo.objects.all()
    serializer_class = TodoSerializer
    todo = Todo.objects.first()
    post_request_signal.send(sender=None, request="POST")
    
    for todo in todos:
        title = todo.title
        desc = todo.description
        number.append(desc)
        
        filter.append(title)
        number.append(desc)
        print(number[len(number)-1])
        print (filter[len(filter)-1])
        
    
    
    


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


