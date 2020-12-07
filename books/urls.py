from django.urls import path
from .views import BookAPIView, CreateBookAPIView, UpdateBookAPIView, DetailBookAPIView, DeleteBookAPIView, TodoCreateListViewAPI, TodoUpdateRetriveDeleteAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('create-book/', CreateBookAPIView.as_view(), name='create_book'),
    path('update-book/<int:pk>/', UpdateBookAPIView.as_view(), name='update_book'),
    path('book/<int:pk>/', DetailBookAPIView.as_view(), name='book_details'),
    path('delete-book/<int:pk>/', DeleteBookAPIView.as_view(), name='delete_book'),
    path('todo/', TodoCreateListViewAPI.as_view(), name='todo'),
    path('todo/<int:pk>/', TodoUpdateRetriveDeleteAPIView.as_view(), name='todo_urd'),
]
