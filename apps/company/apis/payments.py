from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Payment, SansConfig
from apps.company.serializers.payments import (
    PaymentBackofficeSerializer, PaymentTotalBackofficeSerializer
)
from reservations.core.pagination import CustomPageNumberMorePagination


class PaymentBackofficeViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               GenericViewSet):
    """
        API endpoint that allows payments to be viewed
    """
    queryset = Payment.objects.all()
    serializer_class = ()
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomPageNumberMorePagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    filterset_fields = [
        'reservation__date', 'reservation__time', 'reservation__company', 'status',
    ]
    search_fields = ['reservation__company__name']
    ordering = ('reservation__date', 'reservation__time',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(reservation__company__user=self.request.user)

    def get_serializer_class(self):
        return PaymentBackofficeSerializer


class PaymentTotalBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentTotalBackofficeSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated, ]
    filterset_fields = [
        'reservation__date', 'reservation__time', 'reservation__company', 'status',
    ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(reservation__company__user=self.request.user)

    def list(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.serializer_class(filtered_queryset, many=True).data

        total_amount = sum(i['amount'] for i in serialized_data)

        return Response({'total_amount': total_amount})


class DetailPaymentTotalBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
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
        filtered_queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.serializer_class(filtered_queryset, many=True).data

        total_amount = sum(i['amount'] for i in serialized_data)

        return Response({
            'results': self.serializer_class(filtered_queryset, many=True).data,
            'total_amount': total_amount,

        })
