from .views import PostListApiview, CateoryViewSet, PostDetail, PostViewSet, UserList, UserDetail

from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('category', CateoryViewSet)

urlpatterns = [
    path('post/', PostListApiview.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('users/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
] + router.urls
