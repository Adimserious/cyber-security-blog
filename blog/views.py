from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Blog_post, Category, Comment
from . import forms
from .forms import CommentPost, CreatePost, PostSearchForm, CreateCategory
from django.urls import reverse_lazy


@login_required
def like_view(request, slug, pk):
    """
    Handle liking and unliking a post based on the slug and primary key.
    """
    post = get_object_or_404(Blog_post, pk=pk)

    if post.likes.filter(pk=request.user.pk).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(post.get_absolute_url())


def post_search(request):
    """
    Search view for blog posts
    """
    form = PostSearchForm(request.GET or None)
    q = ''
    results = []

    if form.is_valid():
        q = form.cleaned_data['q']
        results = Blog_post.objects.filter(
            Q(title__icontains=q) | Q(body_content__icontains=q)  # Search in title and content
        )

    return render(request, 'blog/search.html', {
        'form': form,
        'q': q,
        'results': results
    })


class AllPost(generic.ListView):
    """
    Display all published posts with pagination.
    """
    queryset = Blog_post.objects.filter(status=1).order_by('-created')
    template_name = "blog/all_post.html"
    paginate_by = 6


class CategoryListView(generic.ListView):
    """
    Display posts by category.
    """
    template_name = "blog/create_category.html"
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return Blog_post.objects.filter(
            category__slug=category_slug, status=1
        ).order_by('-created')


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Blog_post, pk=pk)

    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('home')

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You don't have permission to delete this comment.")
        return redirect('home')

    if request.method == "POST":
        post_slug = comment.post.slug  # Get the slug of the related post
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('read_more', slug=post_slug)  # Redirect back to the post

    return render(request, 'blog/delete_comment.html', {'comment': comment})


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You don't have permission to edit this comment.")
        return redirect('home')

    if request.method == "POST":
        form = CommentPost(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('read_more', slug=comment.post.slug)  # Redirect to the post after saving
    else:
        form = CommentPost(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def edit_post(request, pk):
    """
    Edit a blog post.
    """
    post = get_object_or_404(Blog_post, pk=pk)

    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('home')

    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated Successfully!')
            return redirect(post.get_absolute_url())  # Redirect to the post's detail page after updating
    else:
        form = CreatePost(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


def read_more(request, slug):
    """
    Display a detailed post view with comments and likes.
    """
    post = get_object_or_404(Blog_post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created")
    like_count = post.likes.count()
    user_liked = request.user in post.likes.all() if request.user.is_authenticated else False

    # Check if user its coming from search results
    q = request.GET.get('q')  # Get the search query from the GET parameters
    from_search = request.GET.get('from_search')

    if request.method == "POST":
        comment_form = CommentPost(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment Submitted for Approval')
    else:
        comment_form = CommentPost()

    return render(request, 'blog/read_more.html', {
        "post": post,
        "comments": comments,
        "like_count": like_count,
        "comment_form": comment_form,
        "user_liked": user_liked,
        "q": q,
        "from_search": from_search,
    })


@login_required(login_url="/accounts/login/")
def create_post(request):
    """
    View to create a blog post.
    """
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post Created Successfully! Waiting for approval.')
            return redirect('home')
    else:
        form = CreatePost()

    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def create_category(request):
    """
    View to create a category.
    """
    if request.method == "POST":
        form = CreateCategory(request.POST)
        if form.is_valid():
            # Check if the category with the same name already exists
            name = form.cleaned_data.get('name')
            if Category.objects.filter(name__iexact=name).exists():
                messages.error(request, f'Category "{name}" already exists. Please choose another name.')
            else:
                category = form.save(commit=False)
                category.author = request.user
                category.save()
                messages.success(request, "Category Created Successfully!")
                return redirect('category_list')
    else:
        form = CreateCategory()

    return render(request, 'blog/create_category.html', {'form': form})


@login_required
def category_list(request):
    """
    View to list all categories.
    """
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


@login_required
def update_category(request, pk):
    """
    View to update a category. Only the category's author can update it.
    """
    category = get_object_or_404(Category, pk=pk)
    
    # Ensures the logged-in user is the author
    if category.author != request.user:
        messages.error(request, "You are not authorized to edit this category.")
        return redirect('category_list')

    if request.method == "POST":
        form = CreateCategory(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Updated Successfully!")
            return redirect('category_list')
    else:
        form = CreateCategory(instance=category)

    return render(request, 'blog/update_category.html', {'form': form, 'category': category})


@login_required
def delete_category(request, pk):
    """
    View to delete a category. Only the category's author can delete it.
    """
    category = get_object_or_404(Category, pk=pk)

    # Ensures the logged-in user is the author
    if category.author != request.user:
        messages.error(request, "You are not authorized to delete this category.")
        return redirect('category_list')

    if request.method == "POST":
        category.delete()
        messages.success(request, "Category Deleted Successfully!")
        return redirect('category_list')

    return render(request, 'blog/delete_category.html', {'category': category})
