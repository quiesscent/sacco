import string
import random
from .models import CustomUser
from django.conf import settings

# Create your views here.

def generate_unique_membership_number():
    characters = string.ascii_uppercase + string.digits
    while True:
        membership_number = ''.join(random.choices(characters, k=6))
        if not CustomUser.objects.filter(membership_no=membership_number).exists():
            return membership_number
