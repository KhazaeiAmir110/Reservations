from django.urls import path

from .views import ProfileView

app_name = 'user_dashboard'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
]
