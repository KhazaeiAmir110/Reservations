from rest_framework.routers import DefaultRouter

from apps.company.apis.v1.fake_apis import (
    CompanyBackOfficeTestViewSet, ReservationBackOfficeTestViewSet, PaymentBackOfficeTestViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackOfficeTestViewSet, basename='company-test')
router.register(r'api/reservation', ReservationBackOfficeTestViewSet, basename='reservation-test')
router.register(r'api/payment', PaymentBackOfficeTestViewSet, basename='payment-test')

urlpatterns = router.urls
