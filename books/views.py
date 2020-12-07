from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class TodoCreateListViewAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateRetriveDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
