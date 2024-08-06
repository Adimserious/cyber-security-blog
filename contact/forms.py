from django import forms
from .models import RequestContact


class RequestContactForm(forms.ModelForm):
    class Meta:
        model = RequestContact
        fields = ("name", "email", "message")
