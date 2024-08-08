from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentPost
from .models import Blog_post

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Blog_post(title="Blog title", author=self.user,
                         slug="blog-title", snippet="Blog snippet",
                         body_content="Blog body_content", status=1)
        self.post.save()

    def test_render_read_more_page_with_comment_post(self):
        response = self.client.get(reverse(
            'read_more', args=['blog-title']))
        print(response.body_content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.body_content)
        self.assertIn(b"Blog body_content", response.body_content)
        self.assertIsInstance(
            response.context['comment_post'], CommentPost)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'read_more', args=['blog']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )