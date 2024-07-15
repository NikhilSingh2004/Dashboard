from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import UserProfile

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user_profile = UserProfile.objects.get(username=username)
            if user_profile.check_password(password):
                return user_profile
            else:
                return None
        except UserProfile.DoesNotExist:
            return None
        except Exception as e:
            return None
