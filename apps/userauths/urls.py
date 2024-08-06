from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRegisterView, UserLoginView, UserLogoutView
from apps.userauths.api.api import UserViewSet, UserLoginViewSet

app_name = 'userauths'

router = DefaultRouter()
# router.register(r'', UserLoginViewSet, basename='api-users')
# router.register(r'login', UserLoginView, basename='api-login')

urlpatterns = [
    path('api/', UserLoginViewSet.as_view()),
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
