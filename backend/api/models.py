from django.db import models
from users.models import CustomUser
from .logic import *
from django.utils.crypto import get_random_string

def generate_unique_uid():
    return get_random_string(7)

class Otp(models.Model) :
    email = models.EmailField(max_length=254, unique=True)
    otp = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.email

class Document(models.Model) :
    uid = models.CharField(
        max_length=7,
        unique=True,
        default=generate_unique_uid,
        editable=False
    )
    fileName = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    createdat = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fileName} - {self.uid}"

class Report(models.Model):
    uid = models.CharField(
        max_length=7,
        unique=True,
        default=generate_unique_uid,
        editable=False
    )
    title = models.CharField(max_length=1000)
    content = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.uid}"

class Message(models.Model):
    uid = models.CharField(
        max_length=7,
        unique=True,
        default=generate_unique_uid,
        editable=False
    )
    senderIsUser = models.BooleanField()
    content = models.CharField(max_length=10000)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uid