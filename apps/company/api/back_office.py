from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation
from apps.company.serializers import (
    CompanyBackOfficeSerializer, ReservationBackOfficeSerializer
)


class CompanyBackOfficeViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               GenericViewSet):
    """
        API endpoint that allows companies to be viewed
    """
    queryset = Company.objects.all()
    serializer_class = CompanyBackOfficeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ReservationBackOfficeViewSet(mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   GenericViewSet):
    """
        API endpoint that allows reservations to be viewed
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationBackOfficeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(company__user=self.request.user)
