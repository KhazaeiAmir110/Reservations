from rest_framework.routers import DefaultRouter

from apps.userauths.api.profile import UserDashboardHeaderApi

router = DefaultRouter()
router.register(r'api/user_header', UserDashboardHeaderApi, basename='user_header')

urlpatterns = router.urls
