from rest_framework import serializers
from posts.models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        queryset = get_user_model().objects.all(), slug_field = "username"
    )
    post_id = serializers.IntegerField(source = 'id', read_only = True)

    class Meta: 
        model = Post
        fields = [
            'post_id',
            'author',
            'title',
            'body'
        ]