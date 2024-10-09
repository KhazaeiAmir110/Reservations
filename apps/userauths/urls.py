from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.userauths.api.api import (
    UserLoginVApi, UserLogoutApi, UserRegisterApi, UserDashboardHeaderApi, UserDashboardApi
)
from .views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

router = DefaultRouter()
router.register(r'api/login', UserLoginVApi, basename='login')
router.register(r'api/logout', UserLogoutApi, basename='logout')
router.register(r'api/register', UserRegisterApi, basename='register')

router.register(r'api/user_header', UserDashboardHeaderApi, basename='user_header')
router.register(r'api/user_dashboard', UserDashboardApi, basename='user_dashboard')

urlpatterns += router.urls
