from rest_framework import status
from .logic import *
from django.db.models import Q
from django.conf import settings

from .models import *
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import *

class showMe(APIView) :
    def get(self, request) :
        user = self.request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmailVerification(APIView) :
    OTP = None

    def get(self, request) :
        user_email = self.request.user.email
        self.OTP = generate_otp()
        try :
            emailstatus = send_mail(
                "email verification",
                f"Your OTP to verify email in FriendsBook is {self.OTP}, dont share with any one",
                settings.EMAIL_HOST_USER,
                [user_email],
                fail_silently=False,
            )
            try:
                already_exists = Otp.objects.filter(email=user_email).exists()
                if Otp.objects.filter(email=user_email).exists() :
                    x = Otp.objects.get(email=user_email)
                    x.otp = str(self.OTP)
                    x.save()
                else :
                    Otp.objects.create(email = user_email, otp = str(self.OTP))
            except Exception as e :
                print(e)

        except :
            return Response("error")
        return Response("success")
    
    def post(self, request) :
        user_email = self.request.user.email
        recieved_otp = str(request.data["otp"])
        print("===============")
        print(user_email)
        print(request.data)
        print("===============")
        actual_otp = None
        try :
            x = Otp.objects.get(email = user_email)
            actual_otp = str(x.otp)
        except :
            return Response("otp request not found, first get email verification otp.")

        check = True if recieved_otp==actual_otp else False

        if check :
            user = CustomUser.objects.get(email = user_email)
            user.verified = True
            # Otp.objects.get(email = user_email).delete()
            user.save()
            return Response({"status" : "verified"})
        else :
            return Response(f"some error occured")
