import string
import random
from django.shortcuts import get_object_or_404
from .models import CustomUser, MemberDependent
from django.conf import settings

# Create your views here.

def generate_unique_membership_number():
    characters = string.digits
    while True:
        membership_number = ''.join(random.choices(characters, k=6))
        if not CustomUser.objects.filter(member_no=membership_number).exists():
            return membership_number

def verify_dependant(id):
    dependant = get_object_or_404(MemberDependent, id=id)
    dependant.verified = True
    dependant.save()
