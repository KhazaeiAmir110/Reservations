from rest_framework.routers import DefaultRouter

from apps.company.apis.company import (
    CompanyBackofficeViewSet, ListCompanySummaryBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackofficeViewSet, basename='company_base')
router.register(r'api/listCompanySummary', ListCompanySummaryBackofficeViewSet, basename='company_summary')

urlpatterns = router.urls
