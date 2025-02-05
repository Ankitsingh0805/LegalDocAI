from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('showme/', views.showMe.as_view(), name="showme"),
    path('verifymyemail',views.EmailVerification.as_view(), name="get email otp"),
]

# document urls :
urlpatterns += [
    path('document/', views.DocumentOperations.as_view(), name="document-upload"),
    path('document/<slug:uid>/', views.DocumentOperations.as_view(), name="document-get"),
    path('document/', views.DocumentOperations.as_view(), name="document-get-all"),
    path('document/<slug:uid>/', views.DocumentOperations.as_view(), name="document-delete"),
]

# report urls :
urlpatterns += [
    # path('report/', views.ReportOperations.as_view(), name="report"),
]

# message urls :
urlpatterns += [
    # path('message/', views.MessageOperations.as_view(), name="message"),
]