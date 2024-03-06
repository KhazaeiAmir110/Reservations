from django.urls import path

from .views import RegisterView

app_name = 'userauths'

urlpatterns = [
    path('sing-up/',RegisterView,name='sing-up'),
    # path('login/', )
]