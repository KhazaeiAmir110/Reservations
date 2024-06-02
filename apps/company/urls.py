from django.urls import path

from .views import HomeView, CompanyDetailView, CompanyListView, CompanyDetail

app_name = 'company'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('detail/<slug:company_slug>/', CompanyDetailView.as_view(), name='detail-company'),
    path('detail/<slug:company_slug>/<str:date_time>/', CompanyDetailView.as_view(), name='work_hours')
]

# Baraato
urlpatterns += [
    path('baraato/', CompanyListView.as_view(), name='list-company'),
    path('baraato/<slug:slug>/', CompanyDetail.as_view(), name='detail-company-baraato')
]
