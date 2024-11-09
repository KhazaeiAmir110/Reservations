from django.urls import path

from apps.company.views import CompanyListView, CompanyDetailView, PaymentView, VerifyPaymentView, send_code

# Baraato
urlpatterns = [
    path('send/', send_code, name='send-code'),
    path('', CompanyListView.as_view(), name='list-company'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='detail-company-baraato'),
    path('<slug:slug>/paymentview/', PaymentView.as_view(), name='payment_view'),
    path('payment/verify/', VerifyPaymentView.as_view(), name='verify_payment'),
]
