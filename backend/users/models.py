from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    pfp = models.ImageField(upload_to="pfps", max_length=None, default="/pfps/default.png", blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    verified = models.BooleanField(default=False , blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
