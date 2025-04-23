from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, phone_number, password, username = None, **extra_fields):
        if not email and not phone_number:
            raise ValueError(_('The Email or phone number must be set'))
        email = self.normalize_email(email)
        if email:
            if not username:
                username = email
        elif phone_number:
            if not username:
                username = phone_number

        user = self.model(username = username, email=email, phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, email=username, phone_number=username, password=password, **extra_fields)