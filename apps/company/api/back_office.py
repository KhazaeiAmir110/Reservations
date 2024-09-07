from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company, Reservation
from apps.company.serializers import CompanyBackOfficeSerializer, ReservationBackOfficeSerializer


class CompanyBackOfficeViewSet(GenericViewSet):
    """
        API endpoint that allows companies to be viewed
    """
    queryset = Company.objects.all()
    serializer_class = CompanyBackOfficeSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        queryset = self.queryset.filter(user=request.user)
        if queryset:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response({"message": "The user does not exist or there is no data"}, status=401)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Company, user=request.user, id=pk)
        if queryset:
            serializer = self.serializer_class(queryset)
            return Response(serializer.data)
        return Response({"message": "The user does not exist or there is no data"}, status=401)


class ReservationBackOfficeViewSet(GenericViewSet):
    """
        API endpoint that allows reservations to be viewed
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationBackOfficeSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        queryset = self.queryset.filter(company__user=request.user)
        if queryset:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response({"message": "The user does not exist or there is no data"}, status=401)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Reservation, company__user=request.user, id=pk)
        if queryset:
            serializer = self.serializer_class(queryset)
            return Response(serializer.data)
        return Response({"message": "The user does not exist or there is no data"}, status=401)
