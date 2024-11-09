from .backoffice import urlpatterns as backoffice_urlpatterns
from .urls_templates import urlpatterns as templates_urlpatterns

app_name = 'userauths'

urlpatterns = []
urlpatterns += backoffice_urlpatterns
urlpatterns += templates_urlpatterns
