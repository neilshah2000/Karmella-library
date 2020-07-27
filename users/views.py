from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import MyUserSerializer

class GetUser(APIView):
 
    def get(self, request, format=None):
        serializer = MyUserSerializer(request.user)
        return Response(serializer.data)