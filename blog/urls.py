from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, about, post_single, post_form, PostViewSet

router = DefaultRouter()
router.register('post',PostViewSet, basename='post')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('new/', post_form, name = 'create'),
    path('<int:pk>/', post_single, name = 'single'),
    path('api/', include(router.urls)),
    # path('api/post/list', PostViewSet.as_view({'get' : 'list'}))
] 
