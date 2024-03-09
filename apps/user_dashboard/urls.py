from django.urls import path

from .views import ProfileView, CreateCompanyView

app_name = 'user_dashboard'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('create/', CreateCompanyView.as_view(), name='create'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
]
