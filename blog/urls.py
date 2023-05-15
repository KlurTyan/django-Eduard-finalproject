from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import index, about, post_single, post_form, TokenObtainPairView, TokenRefreshView, RegisterView, PostViewSet, UserView, CourierView, SelleView, SuperAdminView, BasicView, AssemblerView

router = DefaultRouter()
router.register('post',PostViewSet, basename='post')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('new/', post_form, name = 'create'),
    path('<int:pk>/', post_single, name = 'single'),
    path('api/', include(router.urls)),
    
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),

    path('register/',RegisterView.as_view({'post':'create'})),
    path('user/me/',UserView.as_view({'get':'get_current_user'})),

    path('courier/get/',CourierView.as_view()),
    path('seller/get/',SelleView.as_view()),
    path('assembler/get/',AssemblerView.as_view()),
    path('superadmin/get/',SuperAdminView.as_view()),
    path('basic/get/',BasicView.as_view())

    # path('api/post/list', PostViewSet.as_view({'get' : 'list'}))
] 
