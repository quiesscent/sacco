from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    id_number = models.CharField(max_length=50, unique=True)
    member_no = models.CharField(max_length=100, unique=True)
    profile = models.ImageField(upload_to='profiles/', default='default.jpg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_number', 'member_no']

    class Meta:
        verbose_name_plural ='Members'

    def __str__(self):
        return self.email

class MemberDependent(models.Model):
    '''Model definition for MemberProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=100)
    relationship = models.CharField(default='', max_length=100)
    proof = models.FileField(upload_to='dependents/', default='')
    verified = models.BooleanField(default=False)

    class Meta:
        '''Meta definition for Member Dependent.'''

        verbose_name = 'Member Dependent'
        verbose_name_plural = ' Member  Dependents'

    def __str__(self):
        return f'{self.user.username }, {self.relationship } Information'

class MemberProfile(models.Model):
    '''Model definition for MemberProfile.'''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(default=0)
    residence = models.CharField(default='', max_length=50)

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

class Contributions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    funeral_kitty = models.IntegerField()
    monthly_contributions = models.IntegerField()
    savings = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Contributions'

    def __str__(self):
        return f'{self.user.username} contributions over time'



class OverallContribution(models.Model):
    funeral_kitty = models.IntegerField()
    monthly_contributions = models.IntegerField()
    expenditure = models.IntegerField()
    savings =  models.IntegerField()


    def update_contribution(self):
        contributions = Contributions.objects.all()
        total_kitty = sum(contribution.funeral_kitty for contribution in contributions)
        total_monthly_contributions = sum(contribution.monthly_contributions for contribution in contributions)
        total_savings = sum(contribution.savings for contribution in contributions)

        self.total_contributions = total_kitty
        self.monthly_contributions = total_monthly_contributions
        self.savings = total_savings
        self.save()

    def __str__(self):
        return f'Contribution Statistics'
