from rest_framework import generics
from posts.models import Post
from posts.v1.serializers import PostSerializer
from posts.v1.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class PostList(generics.ListCreateAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    queryset =  Post.objects.all()
    serializer_class = PostSerializer


