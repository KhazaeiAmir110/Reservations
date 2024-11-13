from rest_framework.routers import DefaultRouter

from apps.company.api.back_office import (
    PaymentBackOfficeViewSet, PaymentTotalBackofficeViewSet,
)
from apps.company.apis.company import CompanyBackOfficeViewSet
from apps.company.apis.reservations import (
    ReservationBackOfficeViewSet, ListItemsFilterReservationsBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackOfficeViewSet, basename='company')
router.register(r'api/reservation', ReservationBackOfficeViewSet, basename='reservation')
router.register(r'api/payment', PaymentBackOfficeViewSet, basename='payment')
router.register(r'api/total', PaymentTotalBackofficeViewSet, basename='total-payment')

router.register(r'api/filter/list-companies', ListItemsFilterReservationsBackofficeViewSet,
                basename='filter-list-companies')

urlpatterns = router.urls
