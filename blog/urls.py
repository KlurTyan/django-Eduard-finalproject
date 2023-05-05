from django.urls import path, include
from .views import index, about, post_single

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('<int:pk>/', post_single, name = 'single')
] 
