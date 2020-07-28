from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('', views.blog, name='blog'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]




