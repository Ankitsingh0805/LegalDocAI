from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('showme/', views.showMe.as_view(), name="showme"),
    path('verifymyemail',views.EmailVerification.as_view(), name="get email otp"),
]