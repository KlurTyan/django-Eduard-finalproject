from django.shortcuts import render, redirect
from .models import Post, AboutUS

def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', {'posts' : news})

def about(request):
    aboutPost = AboutUS.objects.last()
    return render(request, 'about.html', {'about' : aboutPost})