from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation, Payment
from apps.company.serializers import (
    CompanyBackOfficeSerializer, ReservationBackOfficeSerializer, PaymentBackOfficeSerializer,
)
from reservations.core.pagination import CustomPageNumberPagination


# Company
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
    serializer_class = ()
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberPagination
    ordering = ('name',)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        return CompanyBackOfficeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationBackOfficeViewSet(mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.CreateModelMixin,
                                   mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin,
                                   GenericViewSet):
    """
        API endpoint that allows reservations to be viewed
    """
    queryset = Reservation.objects.all()
    serializer_class = ()
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberPagination
    ordering = ('date', 'time',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('date', 'time', 'company',)

    def get_queryset(self):
        return self.queryset.filter(company__user=self.request.user)

    def get_serializer_class(self):
        return ReservationBackOfficeSerializer


class PaymentBackOfficeViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               GenericViewSet):
    """
        API endpoint that allows payments to be viewed
    """
    queryset = Payment.objects.all()
    serializer_class = ()
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'reservation__date', 'reservation__time', 'reservation__company', 'status',
    )

    def get_queryset(self):
        return self.queryset.filter(reservation__company__user=self.request.user)

    def get_serializer_class(self):
        return PaymentBackOfficeSerializer
