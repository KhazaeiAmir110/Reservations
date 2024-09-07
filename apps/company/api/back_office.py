from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.company.models import Company
from apps.company.serializers import CompanyBackOfficeSerializer


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
