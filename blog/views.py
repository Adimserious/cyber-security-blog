from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from .models import Blog_post, Category, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from .forms import CommentPost, CreatePost
from django.db.models import Count



# Create your views here.

def like_view(request, slug, pk):
   # grap the post_id from the like button in read_more.html
   post = get_object_or_404(Blog_post, id=request.POST.get('post_id'))
   post.likes.add(request.user)
   return render(
        request,
        "blog/read_more.html",
        # this is a context to pass data from my view to template. the post object is used in the template as DTL variable
        {"post": post,}
    )



class AllPost(generic.ListView):
    
    queryset = Blog_post.objects.filter(status=1)
    template_name = "blog/all_post.html"
    paginate_by = 6


class Category(generic.ListView):
    queryset = Blog_post.objects.filter(author=1)
    template_name = "blog/all_post.html"
    paginate_by = 3


class PostDeleteView(generic.DeleteView):
    queryset = Blog_post.objects.filter(author=1)
    template_name = "blog/delete_post.html"
    success_url = '/'
   
    def test_funs(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
        return HttpResponseRedirect(reverse('home'))
        

"""
def delete_post(request, pk):
    
    view to delete post
    

    queryset = Blog_post.objects.filter(status=1)
    post = get_object_or_404(Blog_post, pk=pk)

    if post.author == request.user:
        return render(request, 'blog/delete_post.html')
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    elif request.user != post.author:
        messages.add_message(request, messages.ERROR, 'You can only delete your own post!')

    
    else:
        return HttpResponseRedirect(reverse('home'))

"""

@login_required
def edit_comment(request, pk):
    """
    Edit comments view
    """
    post = get_object_or_404(Blog_post, pk=pk)


    if request.method == "POST":

        queryset = Blog_post.objects.filter(status=1)
        
        
        comment_post = CommentPost(data=request.POST, instance=post)

        if comment_post.is_valid() and comment.author == request.user:
            comment = comment_post.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return redirect('read_more')

        elif request.user != comment.author:
            return redirect('read_more')

    else: 
        return render(request, 'blog/edit_comment.html', {'comment_post': comment_post})
    



def edit_post(request, pk):
    """
    Edit post view
    """
    post = get_object_or_404(Blog_post, pk=pk)

    if request.method == "POST":

        form = CreatePost(request.POST, instance=post)
        # Associating a post being created with the logged in user
        if form.is_valid() and post.author == request.user:
            
            post =  form.save(commit=False)
            post.post = post
            post.approved = False
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'All done! Post is Updated')
            return redirect('home')

        elif request.user != post.author:
            return redirect('home')
            
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    
    else: 
        form = CreatePost(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form})




def read_more(request, slug,):
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

    likes = post.likes.all()
    like_count = post.likes.count()
    
    

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
        "comment_post": comment_post,
        "like_count": like_count},

    )


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




def create_category(request):
    """
    Renders the Category page
    """
    if request.method == "POST":
        category_form = forms.CreatCategory(data=request.POST)
        if category_form.is_valid():
            category_form =  category_form.save(commit=False)
            category_form.author = request.user
            category_form.save()
            messages.add_message(request, messages.SUCCESS, "All done, New category added! awaiting approval.")
            return redirect('home')
    
    else:
        category_form = forms.CreatCategory()
        # new instance of the create category form to render to the user
    return render(request, 'blog/create_category.html', {'category_form': category_form})
