from rest_framework.routers import DefaultRouter

from apps.userauths.api.api import (
    UserLoginVApi, UserLogoutApi, UserRegisterApi, UserDashboardHeaderApi
)

router = DefaultRouter()
router.register(r'api/login', UserLoginVApi, basename='login')
router.register(r'api/logout', UserLogoutApi, basename='logout')
router.register(r'api/register', UserRegisterApi, basename='register')

router.register(r'api/user_header', UserDashboardHeaderApi, basename='user_header')

urlpatterns = router.urls
