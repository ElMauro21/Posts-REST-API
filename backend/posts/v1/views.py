from rest_framework import viewsets
from posts.models import Post
from django.contrib.auth import get_user_model
from posts.v1.serializers import PostSerializer , UserSerializer
from posts.v1.permissions import IsOwnerOrReadOnly
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    queryset =  Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


