from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import CreateCategory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect




# Create your views here.
def category(request):
    """
    Renders the Category page
    """
    if request.method == "POST":
        category_form = RequestCategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form =  category_form.save(commit=False)
            category_form.author = request.user
            category_form.save()
            messages.add_message(request, messages.SUCCESS, "All done,  Add category received! awaiting approval.")
    
    category_form = RequestCategoryForm()

    return render(
        request,
        "create_category/category.html",
        {"category_form": category_form,},
    )
