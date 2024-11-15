from rest_framework.routers import DefaultRouter

from apps.company.apis.payments import (
    PaymentBackofficeViewSet, PaymentTotalBackofficeViewSet,DetailPaymentTotalBackofficeViewSet
)

router = DefaultRouter()

router.register(r'api/payment', PaymentBackofficeViewSet, basename='payment')
router.register(r'api/payment_total', PaymentTotalBackofficeViewSet, basename='total-payment')
router.register(r'api/payment_total_detail', DetailPaymentTotalBackofficeViewSet, basename='detail-total-payment')

urlpatterns = router.urls
