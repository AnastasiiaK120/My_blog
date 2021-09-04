from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTest(TestCase):
    def setUp(self) -> None:

        test = User.objects.create(username="test", password="test123")
        test.save()

        post = Post.objects.create(author=test, title='Hello test', body="Body test")
        post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        author_bd = post.author

        self.assertEqual(str(author_bd), "test")