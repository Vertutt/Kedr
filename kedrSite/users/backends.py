from email.errors import NonPrintableDefect

from django.utils.text import normalize_newlines

from users.models import CustomUser
from django.db.models import  Q
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth import get_user_model



class CustomAuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_users = False
    supports_inactive_users = False


    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return CustomUser.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return  None

    def authenticate(self, request,username = None, email= None, phone_number = None, password= None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(email=username) | Q(phone_number=username)
            )
        except UserModel.DoesNotExist:
            return None

        return user if user.check_password(password) else None