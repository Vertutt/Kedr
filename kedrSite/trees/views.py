from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from .models import Trees, TreesImages
from .serializers import TreesSerializer, TreesCoordinatesSerializer, TreesImageSerializer

class TreeAPICreate(generics.CreateAPIView):
    serializer_class = TreesSerializer
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request, format=None):
        images = request.FILES.getlist('images', [])
       # print(len(images))
       # request.data.pop('images')
        serialized_data = self.serializer_class(data=request.data)
        tree = None
        
        if serialized_data.is_valid():
          #  print('awdasbewghgferghgfe')
            tree = Trees.objects.create(**serialized_data.data)
        
        image_dict = {}
        if tree and len(images) > 0:
            for image_data in images:
                if not isinstance(image_data, dict):
                    image_dict = {'image': image_data, 'tree': str(tree.id)}
                else:
                    image_dict = image_data.copy()
                    image_dict['tree'] = str(tree.id)

                tree_image_serialized_data = TreesImageSerializer(data=image_dict)
                
                if tree_image_serialized_data.is_valid(raise_exception=True):
                    print(tree_image_serialized_data.data)
                    image_obj = TreesImages.objects.create(**tree_image_serialized_data.validated_data)


        return Response( status=status.HTTP_201_CREATED)


class TreesAPIList(generics.ListCreateAPIView):
    queryset = Trees.objects.all()
    serializer_class = TreesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)





class TreesAPIDetails(generics.RetrieveAPIView):
    queryset = Trees.objects.all()
    serializer_class = TreesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TreesAPICoordinates(generics.ListAPIView):
    queryset = Trees.objects.all()
    serializer_class = TreesCoordinatesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]