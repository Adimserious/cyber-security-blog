from . import views
from django.urls import path


urlpatterns = [
    path('post/<int:pk>', views.edit_post, name='edit_post'),
    path('', views.AllPost.as_view(), name='home'),
    path('create/', views.create_post, name="create"),
    path('create_category/', views.create_category, name='create_category'),
    

    path('<slug:slug>/', views.read_more, name='read_more'),
    
    path('<slug:slug>/edit_comment/<int:comment_id>',views.edit_comment, name='edit_comment'),
    path('<slug:slug>/<int:pk>', views.like_view, name='like_post'),
    

]
