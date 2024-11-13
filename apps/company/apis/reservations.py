from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation
from apps.company.serializers.reservations import (
    ReservationBackOfficeSerializer, ListReservationBackOfficeSerializer,
    ListItemsFilterReservationsBackofficeSerializer
)
from reservations.core.pagination import CustomPageNumberPagination


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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
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
            return ListReservationBackOfficeSerializer
        return ReservationBackOfficeSerializer


# List Filter
class ListItemsFilterReservationsBackofficeViewSet(mixins.ListModelMixin, GenericViewSet):
    """
        Api for list filter reservations
    """
    queryset = Company.objects.all()
    serializer_class = ListItemsFilterReservationsBackofficeSerializer
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
