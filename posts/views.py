from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly  # new


class PostListApiview(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
