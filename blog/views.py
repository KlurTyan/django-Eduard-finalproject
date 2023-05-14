from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer, UserSerializer, PostSerializer, GetUserSerializer
from .models import Post, AboutUS, User
from .forms import PostForm

class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

class RegisterView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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