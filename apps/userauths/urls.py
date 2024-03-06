from django.urls import path

from .views import RegisterView, LoginView, LogoutView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/', RegisterView, name='sing-up'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout')
]
