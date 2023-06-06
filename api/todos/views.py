from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.dispatch import Signal
from rest_framework import generics
from .models import Todo , Back
from .serializers import TodoSerializer, BackSerializer
# Create your views here.

filter = []
number = []
id = []

#Function to delete with an ID 
def delete(todo_id):
    todelete = Todo.objects.get(pk=todo_id)
    todelete.delete()

# Define a custom signal
post_request_signal = Signal()

# Connect a signal handler (here POST) to the custom signal
def my_function(sender, request, **kwargs):

    #Retrieve the data 
    ids = []  
    todos = Todo.objects.all()
    for todo in todos:
        ids.append(todo.pk)
        title = todo.title
        desc = todo.description
        number.append(desc)
        filter.append(title)
        
    if len(ids) > 0:
        for todo_id in ids:
            delete(todo_id)
        print("Deleted")

    # Your logic here

    #POST the new numbers to get them back in the front end 
    print("POST request received")
    url = "http://localhost:8000/api/back/"
    data = {
        "number" : "Data has been",
        "description": "Sent back"
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        # POST request succeeded
        print("POST request successful")
        print("Response:", response.json())
    else:
        # POST request failed
        print("POST request failed")
        print("Status code:", response.status_code)
    
    
#When a post request is signaled, it executes my_function
post_request_signal.connect(my_function)

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def refresh_data(self):
        self.queryset = Todo.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        # Send the post_request_signal after creating a new object
        post_request_signal.send(sender=None, request=self.request)

#Class tthat renders at /api/Id to see a specific element 
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

#Can't remember why it s here exactly 
def my_view(request):
    if request.method == 'POST':
        
      
        #Allows to delete any other post that did not get deleted
        post_request_signal.send(sender=None, request=request)

    else:
        # Handle other HTTP methods (GET, PUT, etc.)
        return HttpResponse("Only POST requests allowed")

#Send back the data 
class DataBack(generics.ListCreateAPIView):
    queryset = Back.objects.all()
    serializer_class = BackSerializer

