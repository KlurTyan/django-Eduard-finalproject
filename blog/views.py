from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import PostSerializer
from rest_framework import mixins

from .models import Post, AboutUS
from.forms import PostForm


class PostViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

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

def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date  = timezone.now()
            post.save()
            return redirect('single', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html',{'form' : form})