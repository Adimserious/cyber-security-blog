from . import views
from django.urls import path


urlpatterns = [
    path('create_category/', views.create_category, name='create_category'),
]

