from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView


class UserLoginViewSet(APIView):
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
