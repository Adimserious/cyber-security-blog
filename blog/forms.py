from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Blog_post
        fields = ['title', 'slug', 'author', 'image', 'body_content', 'snippet', 'category']