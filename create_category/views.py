from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from .models import CreateCategory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms
from .forms import CategoryForm


def create_category(request):
    """
    Renders the Category page
    """
    if request.method == "POST":
        category_form = RequestCategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form =  category_form.save(commit=False)
            category_form.author = request.user
            category_form.save()
            messages.add_message(request, messages.SUCCESS, "All done, New category added! awaiting approval.")
            return redirect('home')
    
    else:
        category_form = RequestCategoryForm()
        # new instance of the create category form to render to the user
    return render(request, 'create_category/category.html', {'category_form': category_form})
