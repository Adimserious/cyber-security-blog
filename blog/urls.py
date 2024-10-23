from django.urls import path
from . import views


urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('search/', views.post_search, name="post_search"),
    path('create/', views.create_post, name="create"),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('edit_comment/<int:pk>/update', views.edit_comment,
         name='edit_comment'),
    path('delete_post/<int:pk>/remove/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('create_category/', views.create_category, name='create_category'),
    path('<slug:slug>/', views.read_more, name='read_more'),
    path('<slug:slug>/<int:pk>', views.like_view, name='like_post'),

]
