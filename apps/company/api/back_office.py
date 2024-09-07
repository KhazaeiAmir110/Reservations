from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.company.models import Company
from apps.company.serializers import CompanyBackOfficeSerializer


class CompanyBackOfficeViewSet(GenericViewSet):
    """
        API endpoint that allows companies to be viewed
    """
    queryset = Company.objects.all()
    serializer_class = CompanyBackOfficeSerializer

    def list(self, request):
        if request.user.is_superuser:
            pass
        elif request.user.is_authenticated:
            queryset = self.queryset.filter(user=request.user)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Not authorized"}, status=401)
