from django.urls import path

from .views import CompanyListView

app_name = 'company'

# Baraato
urlpatterns = [
    path('', CompanyListView.as_view(), name='list-company'),
    path('baraato/<slug:slug>/', CompanyListView.as_view(), name='detail-company-baraato')
]
