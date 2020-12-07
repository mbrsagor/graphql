from rest_framework import generics

from .models import Book, Todo
from .serializers import BookSerializer, TodoSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBookAPIView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteBookAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TodoCreateListViewAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateRetriveDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
