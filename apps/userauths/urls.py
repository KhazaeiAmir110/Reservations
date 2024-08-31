from django.urls import path

from apps.userauths.api.api import UserLoginVApi, UserLogoutApi, UserRegisterApi
from .views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('api/login', UserLoginVApi.as_view(), name='login'),
    path('api/logout', UserLogoutApi.as_view(), name='logout'),
    path('api/register', UserRegisterApi.as_view(), name='register'),
]
