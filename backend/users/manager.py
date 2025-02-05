from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, pfp=None, password=None, password2=None, bio=None):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, pfp=pfp, bio=bio)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user