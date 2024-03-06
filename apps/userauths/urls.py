from django.urls import path

from .views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
