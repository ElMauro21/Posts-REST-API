import pytest
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def test_post(db):
    test_user = User.objects.create_user("test_user","test@example.com","testpassword")
    post = Post.objects.create(
        title = "Test post",
        body = "This a test post",
        author = test_user
    )

    return post

def test_create_post(test_post):
    assert test_post.title == "Test post"
    assert test_post.body == "This a test post"
    assert str(test_post.author) == "test_user"
    assert str(test_post) == "Test post"