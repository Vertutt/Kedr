from rest_framework import serializers
from .models import Trees, TreesImages
import os
class TreesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreesImages
        fields = '__all__'

class TreesSerializer(serializers.ModelSerializer):
    images = TreesImageSerializer(many=True, required=False)
    class Meta:
        model = Trees
        fields = '__all__'
        extra_kwargs = {'owner':{'read_only':True}}

class TreesCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trees
        fields = ['id','latitude', 'longitude']
