from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer
from apps.userauths.models import User


class UserLoginVApi(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'YOU': 'Login'})
        return Response({'YOU': 'NO Login'})

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            return Response({'detail': 'Session login successful.'})
        return Response({'Error': "user is not found"}, status=400)


class UserLogoutApi(APIView):
    def post(self, request):
        logout(request)
        Session.objects.get(session_key=request.session.session_key).delete()
        return Response("Logout")


class UserRegisterApi(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                phone=serializer.validated_data['phone']
            )
            return Response(serializer.data)
        return Response(serializer.errors)
