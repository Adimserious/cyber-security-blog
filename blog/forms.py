from .models import Comment
from django import forms


class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ('body',)