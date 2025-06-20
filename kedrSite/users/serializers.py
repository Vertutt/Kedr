import random
from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name','surname' ,'email', 'phone_number','password']
        extra_kwargs = {'password': {'write_only': True}}