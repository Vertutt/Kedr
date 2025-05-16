from django.template.context_processors import request
from rest_framework import serializers
from .models import Promocode

class PromocodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = '__all__'