from rest_framework.routers import DefaultRouter

from apps.company.apis.company import (
    CompanyBackofficeViewSet, ListCompanySummaryBackofficeViewSet, HolidaysDateBackofficeViewSet,
    SansConfigBackofficeViewSet
)

router = DefaultRouter()
router.register(r'api/company', CompanyBackofficeViewSet, basename='company_base')
router.register(r'api/listCompanySummary', ListCompanySummaryBackofficeViewSet, basename='company_summary')
router.register(r'api/holidaysdate', HolidaysDateBackofficeViewSet, basename='company_holidaysdate')
router.register(r'api/sansconfig', SansConfigBackofficeViewSet, basename='company_sansconfig')

urlpatterns = router.urls
