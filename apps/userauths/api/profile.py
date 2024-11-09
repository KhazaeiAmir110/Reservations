from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.userauths.models import User
from apps.userauths.serializers import (
    UserDashboardHeaderSerializer
)


# Page 1
class UserDashboardHeaderApi(mixins.ListModelMixin, GenericViewSet):
    """
        Api information User for header page 1
    """
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserDashboardHeaderSerializer

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user.username)
