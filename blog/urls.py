from django.urls import path
from . import views

urlpatterns = [
    # assigning view: post_list to th root URL
    path('', views.post_list, name='post_list'),
]