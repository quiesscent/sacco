from django import forms
from .models import MemberProfile

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['mobile_no', 'residence', 'profile_picture']

        widgets = {
            'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}),
            'residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter residence'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
