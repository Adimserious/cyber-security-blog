from django.urls import path
from . import views

# Contact url
urlpatterns = [
    path('', views.contact_me, name='contact'),
]
