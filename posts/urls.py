from .views import PostListApiview, PostDetail, PostViewSet

from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('post/', PostListApiview.as_view(), name='post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
] + router.urls
