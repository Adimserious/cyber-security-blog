from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Blog_post



# Create your views here.
class AllPost(generic.ListView):
    #model = Blog_post
    queryset = Blog_post.objects.all()
    template_name = "blog/all_post.html"
    paginate_by = 3