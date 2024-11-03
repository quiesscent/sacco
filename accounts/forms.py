from django import forms
from .models import MemberProfile, MemberDependent


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['mobile_no', 'residence']

        widgets = {
            'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}),
            'residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter residence'}),
        }


class DependantForm(forms.ModelForm):
    class Meta:
        model = MemberDependent
        fields = ['name', 'relationship', 'proof']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
        }