from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'neighborhood', 'username', 'active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Restante do seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu WhatsApp'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu endereço'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu bairro'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do cliente'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Ativo'}),
        }