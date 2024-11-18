from rest_framework.routers import DefaultRouter

from apps.company.apis.reservations import (
    ReservationBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/reservation', ReservationBackofficeViewSet, basename='reservation')

urlpatterns = router.urls
