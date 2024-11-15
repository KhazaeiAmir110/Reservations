from .company import urlpatterns as company_url
from .urls_templates import urlpatterns as templates_urlpatterns

app_name = 'company'

urlpatterns = []
urlpatterns += company_url
urlpatterns += templates_urlpatterns
