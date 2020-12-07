from rest_framework.serializers import ModelSerializer

from .models import Book, Todo

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'price')


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body', 'created_at', 'updated_at')
