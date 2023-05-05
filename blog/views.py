from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, AboutUS

def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', {'posts' : news})

def about(request):
    aboutPost = AboutUS.objects.last()
    return render(request, 'about.html', {'about' : aboutPost})

def post_single(request, pk):
    # Post.objects.get(pk=pk)
    p = get_object_or_404(Post.objects.all(), pk=pk)
    return render(request, 'post_single.html', {'post' : p})
