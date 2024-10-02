from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class EmailOrIDBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Check if the username provided is an email or an ID number
            if '@' in username:
                user = CustomUser.objects.get(email=username)
            else:
                user = CustomUser.objects.get(id_number=username)
        except CustomUser.DoesNotExist:
            return None

        # Check the password
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
