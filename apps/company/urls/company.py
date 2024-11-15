from rest_framework.routers import DefaultRouter

from apps.company.apis.company import (
    CompanyBackofficeViewSet, ListCompanySummaryBackofficeViewSet, HolidaysDateBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackofficeViewSet, basename='company_base')
router.register(r'api/listCompanySummary', ListCompanySummaryBackofficeViewSet, basename='company_summary')
router.register(r'api/holidaysdate', HolidaysDateBackofficeViewSet, basename='company_holidaysdate')

urlpatterns = router.urls
