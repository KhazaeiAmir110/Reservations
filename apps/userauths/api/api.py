from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from apps.userauths.models import User
from apps.userauths.serializers import UserRegisterSerializer


class UserLogoutApi(APIView):
    """
        Logout API for user authentication
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegisterApi(GenericViewSet):
    """
        Register API for user registration
    """
    serializer_class = UserRegisterSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                User.objects.create_user(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                    phone=serializer.validated_data['phone']
                )
            except Exception:
                raise AuthenticationFailed(detail=_("Incorrect authentication credentials in register."))
        return Response({'detail': _("Register Successful")})
