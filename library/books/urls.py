from django.urls import path
from .views import BookAPIView, CreateBookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='books'),
    path('create-book/', CreateBookAPIView.as_view(), name='create_book'),
]
