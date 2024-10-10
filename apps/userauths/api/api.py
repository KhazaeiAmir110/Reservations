from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework import mixins
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.userauths.models import User
from apps.userauths.serializers import (
    UserRegisterSerializer, UserLoginSerializer, UserDashboardHeaderSerializer
)


# Authentication user
class UserLoginVApi(GenericViewSet):
    """
        Login API for user authentication
    """
    serializer_class = UserLoginSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None and user.is_active:
            login(request, user)
            return Response({'detail': 'Session login successful.'}, status=200)

        raise AuthenticationFailed()


class UserLogoutApi(GenericViewSet):
    """
        Logout API for user authentication
    """
    serializer_class = UserLoginSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        logout(request)
        Session.objects.filter(session_key=request.session.session_key).delete()
        return Response({})


class UserRegisterApi(GenericViewSet):
    """
        Register API for user registration
    """
    serializer_class = UserRegisterSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            phone=serializer.validated_data['phone']
        )
        return Response({})


# Page 1
class UserDashboardHeaderApi(mixins.ListModelMixin, GenericViewSet):
    """
        Api information User for header page 1
    """

    queryset = User.objects.all()
    serializer_class = UserDashboardHeaderSerializer

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user.username)
