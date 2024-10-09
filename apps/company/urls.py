from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CompanyListView, CompanyDetailView, PaymentView, VerifyPaymentView, send_code
from apps.company.api.back_office import (
    CompanyBackOfficeViewSet, ReservationBackOfficeViewSet, PaymentBackOfficeViewSet,
    CompanyDashboardApi,
)

app_name = 'company'

# Baraato
urlpatterns = [
    path('send/', send_code, name='send-code'),
    path('', CompanyListView.as_view(), name='list-company'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='detail-company-baraato'),
    path('<slug:slug>/payment/', PaymentView.as_view(), name='payment_view'),
    path('payment/verify/', VerifyPaymentView.as_view(), name='verify_payment'),
]

# back_office
router = DefaultRouter()
router.register(r'api/company', CompanyBackOfficeViewSet, basename='company')
router.register(r'api/reservation', ReservationBackOfficeViewSet, basename='reservation')
router.register(r'api/payment', PaymentBackOfficeViewSet, basename='payment')
router.register(r'api/company_dashboard', CompanyDashboardApi, basename='company_dashboard')

urlpatterns += router.urls
