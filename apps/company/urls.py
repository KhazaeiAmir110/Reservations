from django.urls import path

from .views import CompanyListView, CompanyDetailView

app_name = 'company'

# Baraato
urlpatterns = [
    path('', CompanyListView.as_view(), name='list-company'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='detail-company-baraato')
]
