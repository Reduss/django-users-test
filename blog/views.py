from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']