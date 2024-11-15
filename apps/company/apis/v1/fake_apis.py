from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apps.company.models import Company, Reservation, Payment
from apps.company.serializers.v1 import (
    CompanyBackOfficeSerializer, PaymentBackOfficeSerializer,
    ListReservationBackOfficeSerializer
)
from reservations.core.pagination import CustomPageNumberAveragePagination


class CompanyBackOfficeTestViewSet(mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   GenericViewSet):
    """
        API Test For Company Back Office.
    """
    queryset = Company.objects.filter(status=Company.StatusEnum.CONFIRMED, )
    serializer_class = CompanyBackOfficeSerializer
    pagination_class = CustomPageNumberAveragePagination

    filter_backends = [filters.OrderingFilter, ]
    ordering = ('name',)


class ReservationBackOfficeTestViewSet(mixins.ListModelMixin,
                                       mixins.RetrieveModelMixin,
                                       GenericViewSet):
    """
        API Test For Reservation Back Office.
    """
    queryset = Reservation.objects.filter(status=Reservation.StatusEnum.CONFIRMED)
    serializer_class = ListReservationBackOfficeSerializer
    pagination_class = CustomPageNumberAveragePagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date', 'time', 'company', ]
    search_fields = ['first_name', 'last_name', 'phone_number', 'company__name']
    ordering = ('date', 'time',)


class PaymentBackOfficeTestViewSet(mixins.ListModelMixin,
                                   GenericViewSet):
    """
        API Test For Payment Back Office.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentBackOfficeSerializer
    pagination_class = CustomPageNumberAveragePagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        'reservation__date', 'reservation__time', 'reservation__company', 'status',
    ]
    ordering = ('reservation__date', 'reservation__time',)
