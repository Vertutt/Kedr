from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from .models import Promocode
from .serializers import PromocodesSerializer
# Create your views here.
class PromocodeConfirmView(APIView):
    serializer_class = PromocodesSerializer
    def get(self, request, promo ):
        try:
            found_promo = Promocode.objects.get(code=promo)
            if found_promo.is_activated == False:
                found_promo.is_activated = True
                found_promo.save()
                return Response(status = status.HTTP_200_OK)
            else:
                return Response({"Content" : "Promocode already used"},status = status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response({"Content" : "Server error"},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

       