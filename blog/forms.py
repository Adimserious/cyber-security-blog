from django import forms
from . import models
from cloudinary.models import CloudinaryField


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Blog_post
        fields = ['title', 'slug', 'image', 'body_content', 'snippet', 'category']





class CommentPost(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)


class CreatCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ("name",)