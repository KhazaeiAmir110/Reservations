from django.contrib.auth import login
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication

from apps.userauths.models import User
from .serializers import UserLoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer


class UserLoginViewSet(APIView):

    def get(self, request, format=None):
        return Response({'test': 'test'})

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'detail': 'Session login successful.'})
        else:
            return Response({'Error': serializer.errors}, status=400)
