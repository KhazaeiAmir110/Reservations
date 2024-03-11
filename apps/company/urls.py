from django.urls import path

from .views import HomeView, CompanyDetailView, WorkTimeView

app_name = 'company'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('detail/<slug:company_slug>/', CompanyDetailView.as_view(), name='detail-company'),
    path('work_time/<slug:company_slug>/<str:date>/', WorkTimeView.as_view(), name='work_hours')
]
