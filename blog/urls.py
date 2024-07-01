from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
]