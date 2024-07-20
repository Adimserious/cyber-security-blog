from . import views
from django.urls import path


urlpatterns = [
    path('', views.CreateCategory, name='create_category'),
]


