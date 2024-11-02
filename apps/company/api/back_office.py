from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation, Payment, SansConfig
from apps.company.serializers import (
    CompanyBackOfficeSerializer, ReservationBackOfficeSerializer, PaymentBackOfficeSerializer,
    ListReservationBackofficeSerializer, PaymentTotalBackofficeSerializer
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

    filter_backends = []
    filterset_fields = []
    search_fields = []
    ordering = ('name',)

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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date', 'time', 'company', ]
    search_fields = ['full_name', 'phone_number']
    ordering = ('date', 'time',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.filterset_fields = ['date', 'time', 'company', 'status', ]
            return self.queryset

        return self.queryset.filter(
            company__user=self.request.user,
            status=Reservation.StatusEnum.CONFIRMED
        )

    def get_serializer_class(self):
        if self.action == 'list':
            return ListReservationBackofficeSerializer
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        'reservation__date', 'reservation__time', 'reservation__company', 'status',
    ]
    search_fields = []
    ordering = ('reservation__date', 'reservation__time',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.search_fields = ['reservation__company__name', ]
            return self.queryset
        return self.queryset.filter(reservation__company__user=self.request.user)

    def get_serializer_class(self):
        return PaymentBackOfficeSerializer


class PaymentTotalBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentTotalBackofficeSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, ]
    filterset_fields = ('status',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(reservation__company__user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        total_amount = SansConfig.objects.filter(
            company__in=queryset.values_list('reservation__company', flat=True)
        ).aggregate(total=Sum('amount'))['total']

        return Response({'total_amount': total_amount})


# Detail Total Payment
class DetailPaymentTotalBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentBackOfficeSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, ]
    filterset_fields = ('status',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(reservation__company__user=self.request.user)

    def list(self, request, *args, **kwargs):
        payments = self.get_queryset()

        if request.query_params.get('status'):
            payments = payments.filter(status=request.query_params.get('status'))

        total_amount = SansConfig.objects.filter(
            company__in=payments.values_list('reservation__company', flat=True)
        ).aggregate(total=Sum('amount'))['total']

        serializer = self.get_serializer(payments, many=True)

        return Response({
            'data': serializer.data,
            'total_amount': total_amount
        })
