from django.urls import path

from .views import ProfileView, CreateCompanyView, ProfileDetailView

app_name = 'user_dashboard'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('create/', CreateCompanyView.as_view(), name='create'),
    path('detail/', ProfileDetailView.as_view(), name='profile-detail'),
]
