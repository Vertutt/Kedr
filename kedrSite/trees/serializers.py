from django.template.context_processors import request
from rest_framework import serializers
from .models import Trees

class TreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trees
        fields = '__all__'
        extra_kwargs = {'owner':{'read_only':True}}

class TreesCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trees
        fields = ['latitude', 'longitude']
