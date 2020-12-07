from django.urls import path
from .views import TodoCreateListViewAPI, TodoUpdateRetriveDeleteAPIView

urlpatterns = [
    path('todo/', TodoCreateListViewAPI.as_view(), name='todo'),
    path('todo/<int:pk>/', TodoUpdateRetriveDeleteAPIView.as_view(), name='todo_urd'),
]
