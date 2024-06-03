from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cyber_blog(request):
    return HttpResponse("Hello, this is the cybersecurity domain Blog!")