from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserLoginSerializer
from apps.userauths.models import User


class UserLoginVApi(APIView):
    """
        Login API for user authentication
    """
    serializer_class = UserLoginSerializer

    def get(self, request):
        if request.user.is_authenticated:
            return Response({'YOU': 'Login'})
        return Response({'YOU': 'NO Login'})

    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response({'detail': 'Session login successful.'})
        return Response({'Error': "user is not found"}, status=400)


class UserLogoutApi(APIView):
    """
        Logout API for user authentication
    """

    def post(self, request):
        logout(request)
        Session.objects.filter(session_key=request.session.session_key).delete()
        return Response("Logout")


class UserRegisterApi(APIView):
    """
        Register API for user registration
    """
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            phone=serializer.validated_data['phone']
        )
        return Response(serializer.data)

