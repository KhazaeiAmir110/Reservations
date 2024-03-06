from django.urls import path

from .views import HomeView, WorkDateView, WorkTimeView

app_name = 'company'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('work_time/<slug:company_slug>/', WorkDateView.as_view(), name='work_time'),
    path('work_time/<slug:company_slug>/<str:date>/', WorkTimeView.as_view(), name='work_hours')
]
