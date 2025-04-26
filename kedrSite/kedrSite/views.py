from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View




class UserConfirmEmailView(View):
    def get(self, request, uid, token):
        userModel = get_user_model()
        try:
            id = urlsafe_base64_decode(uid)
            user = userModel.objects.get(pk=id)
        except (userModel.DoesNotExist): #TypeError, ValueError, OverflowError,  - not working
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('customuser-list')
        else:
            raise 'Email could not be Confirmed'