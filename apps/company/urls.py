from django.urls import path

from .views import HomeView

app_name = 'company'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    # path('login/', )
]
