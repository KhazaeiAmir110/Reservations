from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Reservation
from apps.company.serializers.reservations import (
    CreateORUpdateReservationBackofficeSerializer, ListORRetrieveReservationBackofficeSerializer,
)
from reservations.core.pagination import CustomPageNumberAveragePagination


class ReservationBackofficeViewSet(mixins.ListModelMixin,
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
    pagination_class = CustomPageNumberAveragePagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    filterset_fields = ['date', 'time', 'company', ]
    search_fields = ['first_name', 'last_name', 'phone_number']
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
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateORUpdateReservationBackofficeSerializer
        return ListORRetrieveReservationBackofficeSerializer
