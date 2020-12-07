from django.urls import path
from .views import BookAPIView, CreateBookAPIView, UpdateBookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('create-book/', CreateBookAPIView.as_view(), name='create_book'),
    path('update-book/', UpdateBookAPIView.as_view(), name='update_book'),
]
