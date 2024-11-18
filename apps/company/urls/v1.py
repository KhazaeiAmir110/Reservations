from rest_framework.routers import DefaultRouter

from apps.company.apis.v1.v1 import (
    CompanyBackOfficeViewSet, ReservationBackOfficeViewSet, PaymentBackOfficeViewSet,
    PaymentTotalBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackOfficeViewSet, basename='company')
router.register(r'api/reservation', ReservationBackOfficeViewSet, basename='reservation')
router.register(r'api/payment', PaymentBackOfficeViewSet, basename='payment')
router.register(r'api/total', PaymentTotalBackofficeViewSet, basename='total-payment')

urlpatterns = router.urls
