from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length= 256, unique= True)
    email = models.EmailField(_('email address'), unique= True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number entered in wrong format")
    phone_number = models.CharField(_('phone number'),validators=[phone_regex], unique=True,
                                    max_length=19, null=True)

    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        unique_together = ('username','email', 'phone_number')

    def __str__(self):
        return self.email