from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.views import generic
#from .models import Post/ will remain Post model
from .forms import FormComment


# Create your views here.
def cyber_blog(request):
    return HttpResponse("Hello, this is the cybersecurity domain Blog!")