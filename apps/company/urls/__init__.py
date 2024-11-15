from .company import urlpatterns as company_url
from .reservation import urlpatterns as reservation_url
from .payment import urlpatterns as payment_url
from .urls_templates import urlpatterns as templates_urlpatterns

app_name = 'company'

urlpatterns = []
urlpatterns += company_url
urlpatterns += reservation_url
urlpatterns += payment_url
urlpatterns += templates_urlpatterns
