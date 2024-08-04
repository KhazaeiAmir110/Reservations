from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserRegisterView, UserLoginView, UserLogoutView
from .api.api import UserViewSet

app_name = 'userauths'

router = DefaultRouter()
router.register(r'api', UserViewSet, basename='api-users')

urlpatterns = [
    path('', include(router.urls)),
    path('sing-up/', UserRegisterView.as_view(), name='sing-up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
