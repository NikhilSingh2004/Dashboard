from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    # Custom related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(Group, related_name='user_profiles_custom', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_profiles_custom', blank=True)

    class Meta:
        permissions = (
            ('can_view_profiles', 'Can view user profiles'),
        )
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.username
    