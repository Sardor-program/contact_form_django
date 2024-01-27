from django import forms
from django.core.validators import EmailValidator, integer_validator
from .models import Contact
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'message']


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

