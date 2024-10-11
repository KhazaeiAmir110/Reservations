from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation, Payment, SansConfig
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


class PaymentTotalBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentBackOfficeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status', )

    def list(self, request, *args, **kwargs):
        status = request.query_params.get('status', None)

        payments = self.get_queryset()
        if status:
            payments = payments.filter(status=status)

        total_amount = SansConfig.objects.filter(
            company__in=payments.values_list('reservation__company', flat=True)
        ).aggregate(total=Sum('amount'))['total']

        serializer = self.get_serializer(payments, many=True)

        return Response({
            'payments': serializer.data,
            'total_amount': total_amount
        })
