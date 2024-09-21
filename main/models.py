from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    id_number = models.CharField(max_length=50, unique=True)
    member_no = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_number']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    '''Model definition for UserProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    class Meta:
        '''Meta definition for UserProfile.'''

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return f'{self.user} Profile information'