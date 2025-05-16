from django.template.context_processors import request
from rest_framework import serializers
from .models import Trees, TreesImages

class TreesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreesImages
        fields = '__all__'

class TreesSerializer(serializers.ModelSerializer):
    #images = TreesImageSerializer(many=True, required=False)
    class Meta:
        model = Trees
        fields = '__all__'
        extra_kwargs = {'owner':{'read_only':True}}
    
    def get_images(self, obj):
      images = obj.product_images.all()
      return TreesImageSerializer(images, many=True)

class TreesCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trees
        fields = ['latitude', 'longitude']
