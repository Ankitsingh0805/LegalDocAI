from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser

from .serializers import UserRegistrationSerializer

from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# CORS error :
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status

@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(APIView) :
    def post(self, request) :
        serializer = UserRegistrationSerializer(data = request.data)

        if not serializer.is_valid() :
            return Response({'errors':serializer.errors})
        
        # password = make_password(serializer.validated_data['password'])
        # serializer.validated_data['password'] = password

        serializer.save()

        user = CustomUser.objects.get(username = serializer.data['username'])
        user.save()

        if user.pfp == "" or user.pfp == None:
            user.pfp = "/pfps/default.png"
        
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'payload':serializer.data,'message':"your data has been saved",'refresh_token':str(refresh),'access_token':str(refresh.access_token)})

class SampleEndpoint(APIView) :
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        user = self.request.user
        pfp = None
        if user.pfp :
            pfp = user.pfp
        data = {
            "name" : f"{user.first_name} {user.last_name}",
            "pfp" : f"{pfp}",
            "email" : user.email
        }
        return Response(data)