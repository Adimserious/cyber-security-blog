from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url="/accounts/login/")
class Category(generic.ListView):
    model = Category
    template_name = "blog/category.html"
    paginate_by = 3