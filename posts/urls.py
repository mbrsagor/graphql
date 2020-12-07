from .views import PostListApiview, PostDetail

from django.urls import path

urlpatterns = [
    path('post/', PostListApiview.as_view(), name='post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
