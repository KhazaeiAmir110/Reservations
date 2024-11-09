from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

from apps.userauths.api.api import (
    UserLogoutApi, UserRegisterApi
)

router = DefaultRouter()
router.register(r'api/register', UserRegisterApi, basename='register')

urlpatterns = [
    path('api/login/', ObtainAuthToken.as_view(), name='login'),
    path('api/logout/', UserLogoutApi.as_view(), name='logout'),
]

urlpatterns += router.urls
