from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('', views.Category.as_view(), name='home'),
    path('<slug:slug>/', views.read_more, name='read_more'),
]