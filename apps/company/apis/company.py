from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company
from apps.company.serializers.company import (
    CreateORRetrieveCompanyBackofficeSerializer, ListORDestroyCompanyBackofficeSerializer
)
from core.pagination import CustomPageNumberPagination


class CompanyBackOfficeViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.UpdateModelMixin,
                               GenericViewSet):
    """
        API endpoint that allows companies to be viewed
    """
    queryset = Company.objects.all()
    serializer_class = []
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberPagination

    filter_backends = []
    filterset_fields = [filters.OrderingFilter, ]
    search_fields = []
    ordering = ['name', 'status']

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.filter_backends = [DjangoFilterBackend, filters.SearchFilter]
            self.filterset_fields = ['name', 'status']
            self.search_fields = ['name', 'address']
            return self.queryset

        return self.queryset.filter(
            user=self.request.user,
            status=Company.StatusEnum.CONFIRMED,
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateORRetrieveCompanyBackofficeSerializer
        return ListORDestroyCompanyBackofficeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
