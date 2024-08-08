from django.test import TestCase
from .forms import CommentPost


class TestCommentPost(TestCase):

    def test_post_is_valid(self):
        comment_post = CommentPost({'content': 'Thanks for sharing'})
        self.assertTrue(comment_post.is_valid(), msg='Form is not valid')


    def test_post_is_invalid(self):
        comment_post = CommentPost({'content': ''})
        self.assertFalse(comment_post.is_valid(), msg='Form is valid')