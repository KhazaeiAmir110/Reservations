from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, HolidaysDate, SansConfig, SansHolidayDateTime
from apps.company.serializers.company import (
    CreateORRetrieveCompanyBackofficeSerializer, ListORRetrieveCompanyBackofficeSerializer,
    ListCompanySummaryBackofficeSerializer, HolidaysDateBaseSerializer, CreateORUpdateHolidaysDateSerializer,
    SansConfigBaseBackofficeSerializer, CreateORUpdateSansConfigBackofficeSerializer,
    SansHolidayDateTimeBaseBackofficeSerializer, CreateORUpdateSansHolidayDateTimeBackofficeSerializer
)
from reservations.core.pagination import CustomPageNumberFewerPagination


class CompanyBackofficeViewSet(mixins.ListModelMixin,
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
    pagination_class = CustomPageNumberFewerPagination

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['status']
    search_fields = []
    ordering = ['name', 'status']

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
            self.filterset_fields = ['name', 'status']
            self.search_fields = ['name', 'address']
            return self.queryset

        return self.queryset.filter(user=self.request.user,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateORRetrieveCompanyBackofficeSerializer
        return ListORRetrieveCompanyBackofficeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListCompanySummaryBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    """
        Api for list filter company
    """
    queryset = Company.objects.all()
    serializer_class = ListCompanySummaryBackofficeSerializer
    permission_classes = [IsAuthenticated, ]

    filter_backends = [filters.OrderingFilter, ]
    ordering = ('id',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(
            user=self.request.user,
            status=Company.StatusEnum.CONFIRMED,
        )


class HolidaysDateBackofficeViewSet(mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.DestroyModelMixin,
                                    mixins.UpdateModelMixin,
                                    GenericViewSet):
    """
        API endpoint that allows HolidaysDate to be viewed
    """
    queryset = HolidaysDate.objects.all()
    serializer_class = []
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberFewerPagination

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['date', 'company']
    ordering = ['date']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(
            company__user=self.request.user,
            company__status=Company.StatusEnum.CONFIRMED
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateORUpdateHolidaysDateSerializer
        return HolidaysDateBaseSerializer


class SansConfigBackofficeViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.UpdateModelMixin,
                                  GenericViewSet):
    """
        API endpoint that allows SansConfig to be viewed
    """
    queryset = SansConfig.objects.all()
    serializer_class = []
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberFewerPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.filter_backends = ['company__user']
            return self.queryset
        return self.queryset.filter(
            company__user=self.request.user,
            company__status=Company.StatusEnum.CONFIRMED
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateORUpdateSansConfigBackofficeSerializer
        return SansConfigBaseBackofficeSerializer


class SansHolidayDateTimeBackofficeViewSet(mixins.ListModelMixin,
                                           mixins.RetrieveModelMixin,
                                           mixins.CreateModelMixin,
                                           mixins.DestroyModelMixin,
                                           mixins.UpdateModelMixin,
                                           GenericViewSet):
    """
        API endpoint that allows SansHolidayDateTime to be viewed
    """
    queryset = SansHolidayDateTime.objects.all()
    serializer_class = []
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberFewerPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.filter_backends = ['company__user']
            return self.queryset
        return self.queryset.filter(
            company__user=self.request.user,
            company__status=Company.StatusEnum.CONFIRMED
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateORUpdateSansHolidayDateTimeBackofficeSerializer
        return SansHolidayDateTimeBaseBackofficeSerializer
