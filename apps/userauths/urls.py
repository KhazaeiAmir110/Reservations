from django.urls import path

from apps.userauths.api.api import UserLoginViewSet, UserLogoutView
from .views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('api/login', UserLoginViewSet.as_view(), name='login'),
    path('api/logout', UserLogoutView.as_view(), name='logout'),
]
