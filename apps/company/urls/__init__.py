from django.urls import path, include

from .backoffice import urlpatterns as backoffice_urlpatterns
from .urls_templates import urlpatterns as templates_urlpatterns
from .fake_urls import urlpatterns as backoffice_test_urlpatterns

app_name = 'company'

urlpatterns = []
urlpatterns += backoffice_urlpatterns
urlpatterns += templates_urlpatterns
urlpatterns += [
    path('test/', include(backoffice_test_urlpatterns), name='test'),
]
