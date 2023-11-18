from django import forms
from django.utils.translation import gettext_lazy as _
from yuhutest.apps.users.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        exclude = ('user',)
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'password': _('Password')
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }