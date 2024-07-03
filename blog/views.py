from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Blog_post



# Create your views here.

class Category(generic.ListView):

    
    queryset = Blog_post.objects.filter(author=1)
    template_name = "blog/all_post.html"
    paginate_by = 3


class AllPost(generic.ListView):
    
    queryset = Blog_post.objects.all()
    template_name = "blog/all_post.html"
    paginate_by = 3

def read_more(request, slug):
    """
    Display a detailed post
    
    **Template:**

    :template:`blog/read_more.html`
    """
    queryset = Blog_post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/read_more.html",
        {"post": post},
    )
   