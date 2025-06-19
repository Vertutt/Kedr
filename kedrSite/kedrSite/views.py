from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import redirect



class UserConfirmEmailView(APIView):
    def get(self, request, uid, token):
        userModel = get_user_model()
        try:
            id = urlsafe_base64_decode(uid)
            user = userModel.objects.get(pk=id)
        except :
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(status= status.HTTP_200_OK)
        else:
            return Response({"Content" : "Could not confirm email"},status = status.HTTP_500_INTERNAL_SERVER_ERROR)