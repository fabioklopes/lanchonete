from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'neighborhood', 'customer_code', 'active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'customer_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': ''}),
        }