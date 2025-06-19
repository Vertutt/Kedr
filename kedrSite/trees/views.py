from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db import transaction
from .models import Trees, TreesImages
from promocodes.models import Promocode
from .serializers import TreesSerializer, TreesCoordinatesSerializer, TreesImageSerializer
from django.shortcuts import get_object_or_404
import os
from django.core.files.storage import default_storage
from django.utils import timezone

class TreeAPICreate(generics.CreateAPIView):
    serializer_class = TreesSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, format=None):
        try:
            promo = Promocode.objects.get(code=self.request.POST.get('promo'))
        except:
            return Response({"Content" : "Promocode not found"},status = status.HTTP_404_NOT_FOUND)
        if not promo.is_activated:
            images = request.FILES.getlist('images', [])
            picture = request.FILES['picture']
            serialized_data = self.serializer_class(data=request.data)
            user = None
            tree = None
            if request and hasattr(request, "user"):
                user = self.request.user
            
            if serialized_data.is_valid(raise_exception=True):
                tree = serialized_data.save(owner = user, owner_name =  f"{user.last_name} {user.first_name} {user.surname}")
                ext = os.path.splitext(tree.picture.name)[1]
                tree.picture.name = f"picture_{hash(tree.owner_name)}-{hash(timezone.now())}{ext}"
                tree.save()
            image_dict = {}
            if tree and len(images) > 0:
                for image in images:
                    ext = os.path.splitext(image.name)[1]
                    image.name=f"photo_{hash(tree.owner_name)}-{hash(timezone.now())}{ext}"
                    TreesImages.objects.create(tree=tree, image=image)

            promo.is_activated = True
            promo.save()
            return Response( status=status.HTTP_201_CREATED)
        else: 
            return Response({"Content" : "Promocode already used"},status = status.HTTP_406_NOT_ACCEPTABLE)


class TreeAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trees.objects.all()
    serializer_class = TreesSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Проверка прав доступа
        if request.user != instance.owner and not request.user.is_superuser:
            return Response(
                {"detail": "У вас нет прав на редактирование этого дерева"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        # Обновление основных данных
        self.perform_update(serializer)

        # Обработка новых изображений
        images = request.FILES.getlist('images', [])
        if images:
            for image in images:
                TreesImages.objects.create(tree=instance, image=image)

        return Response(serializer.data)

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Проверка прав доступа
        if request.user != instance.owner and not request.user.is_superuser:
            return Response(
                {"detail": "У вас нет прав на удаление этого дерева"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Удаление связанных изображений и их файлов
        for tree_image in instance.images.all():
            if tree_image.image:
                if default_storage.exists(tree_image.image.name):
                    default_storage.delete(tree_image.image.name)
            tree_image.delete()


        # Удаление основного изображения дерева
        if instance.picture:
            if default_storage.exists(instance.picture.name):
                default_storage.delete(instance.picture.name)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TreeImageAPI(generics.DestroyAPIView):
    serializer_class = TreesImageSerializer
    permission_classes = [IsAuthenticated]
    
    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        image_instance = get_object_or_404(TreesImages, id=self.request.data['image_id'])
        tree = image_instance.tree
        
        # Проверка прав доступа
        if request.user != tree.owner and not request.user.is_superuser:
            return Response(
                {"detail": "У вас нет прав на удаление этого изображения"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Удаление файла изображения
        if image_instance.image:
            if default_storage.exists(image_instance.image.name):
                default_storage.delete(image_instance.image.name)

        image_instance.delete()
        return Response(
            {"detail": "Изображение успешно удалено"},
            status=status.HTTP_204_NO_CONTENT
        )

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