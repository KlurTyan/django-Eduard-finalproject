from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, status, permissions
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .permissions import IsCourier, IsSeller, IsAssembler, IsBasic, IsSuperAdmin
from .serializers import TokenObtainPairSerializer, TokenRefreshSerializer, UserSerializer, PostSerializer, GetUserSerializer, ProductCardSerializer
from .models import Post, AboutUS, User, ProductCard
from .forms import PostForm

class ProductCardView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = ProductCardSerializer
    queryset = ProductCard.objects.all()
    

class CourierView(ListAPIView):
    permission_classes=[IsAuthenticated,IsCourier] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Вы курьер или в народе кура)'}, status=status.HTTP_200_OK)
    
class SelleView(ListAPIView):
    permission_classes =[IsAuthenticated, IsSeller] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Вы являетесь продавцом, вы Барыга?'}, status=status.HTTP_200_OK)

class SuperAdminView(ListAPIView):
    permission_classes=[IsAuthenticated,IsSuperAdmin] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Ты супер мега администратор)'}, status=status.HTTP_200_OK)

class AssemblerView(ListAPIView):
    permission_classes=[IsAuthenticated,IsAssembler] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Вы сборщик?'}, status=status.HTTP_200_OK)

class BasicView(ListAPIView):
    permission_classes=[IsAuthenticated,IsBasic] 

    def get(self, request, *args, **kwargs):
        return Response(data={'success':'Вы покупатель!'}, status=status.HTTP_200_OK)
    

class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer
    def get_permissions(self):
        return super().get_permissions()

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

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[AllowAny]
        else:
            self.permission_classes=[IsAdminUser]
        return super(self.__class__, self).get_permissions()

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