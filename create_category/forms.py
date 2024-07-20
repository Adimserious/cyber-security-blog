from django import forms
from .models import CreateCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CreateCategory
        fields = ("name",)