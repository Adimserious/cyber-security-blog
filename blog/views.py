from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from .models import Blog_post, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from .forms import CommentPost




# Create your views here.



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
    # queryset to filter posts that are done or publiched
    queryset = Blog_post.objects.filter(status=1)
    # this is A helper function. the slug value is unique for each post
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created")
    comment_no = post.comments.filter(approved=True).count()

    if request.method == "POST":
         comment_post = CommentPost(data=request.POST)
         if comment_post.is_valid():
            comment = comment_post.save(commit=False)
            # Associating a comment being created with the logged in user
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        ' All done! Comment is submitted and is waiting approval'
    )
    comment_post = CommentPost()


    return render(
        request,
        "blog/read_more.html",
        # this is a context to pass data from my view to template. the post object is used in the template as DTL variable
        {"post": post,
        "comments": comments,
        "comment_no": comment_no,
        "comment_post": comment_post},
    )


@login_required
def edit_comment(request, slug, comment_id):
    """
    Edit comments view
    """

    if request.method == "POST":

        queryset = Blog_post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_post = CommentPost(data=request.POST, instance=comment)

        if comment_post.is_valid() and comment.author == request.user:
            comment = comment_post.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')

        elif request.user != comment.author:
            return redirect('read_more', args=[slug])

        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    




@login_required(login_url="/accounts/login/")  
def create_post(request):
    """
    Users create post
    
    **Template:**

    :template:`blog/create_post.html`
    """
    if request.method == 'POST':
        form = forms.CreatePost(data=request.POST,)
        if form.is_valid():
            instance =  form.save(commit=False)
            # Associating a post being created with the logged in user 
            instance.author = request.user
            instance.save()
            messages.add_message(
        request, messages.SUCCESS,
        'All done! Post is submitted and is waiting approval'
    )
            return redirect('home')

    
    else:
        # new instance of the create post form to render to the user
        form = forms.CreatePost()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def edit_post(request, slug, post_id):
    """
    Edit post view
    """

    if request.method == "POST":

        queryset = Blog_post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post = get_object_or_404(Blog_post, pk=post_id)

        if post.is_valid() and post.author == request.user:
            post =  post.save(commit=False)
            # Associating a post being created with the logged in user 
            post.author = request.user
            post.save()
            messages.add_message(
        request, messages.SUCCESS,
        'All done! Post is Updated and is waiting approval')
        elif request.user != post.author:
            return redirect('read_more', args=[slug])

        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')
    