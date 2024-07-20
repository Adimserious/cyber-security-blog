from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('create/', views.create_post, name="create"),
    path('create_category/', views.create_category, name='create_category'),
    path('<slug:slug>/', views.read_more, name='read_more'),
    path('<slug:slug>/edit_comment/<int:comment_id>',views.edit_comment, name='edit_comment'),
    path('<slug:slug>/edit_post/<int:post_id>',views.edit_post, name='edit'),
]
