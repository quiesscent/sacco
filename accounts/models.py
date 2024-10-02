from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    id_number = models.CharField(max_length=50, unique=True)
    member_no = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_number']

    def __str__(self):
        return self.email

class MemberDependent(models.Model):
    '''Model definition for MemberProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100)
    relationship = models.CharField(default='', max_length=100)
    proof = models.ImageField(upload_to='dependents/', default='')
    verified = models.BooleanField(default=False)

    class Meta:
        '''Meta definition for Member Dependent.'''

        verbose_name = 'Member Dependent'
        verbose_name_plural = ' Member  Dependents'

    def __str__(self):
        return f'{self.user }, {self.relationship } Information'

class MemberProfile(models.Model):
    '''Model definition for MemberProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(default=0)
    residence = models.CharField(default='', max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', default='')

    class Meta:
        '''Meta definition for MemberProfile.'''

        verbose_name = 'Member Profile'
        verbose_name_plural = 'Member Profiles'

    def __str__(self):
        return f'{self.user.username } Profile'

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} you have a message"