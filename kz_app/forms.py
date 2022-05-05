from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.core.mail import send_mail

from .models import Feedback
from django.forms import *
from django import forms
from django.db import models


class FeedbackCreate(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'author', 'feedback']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of status'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of status'
            }),
            'feedback': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of status'
            })
        }


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 3px solid cyan;'
    }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    phone_num = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    city = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'type': 'password',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'type': 'password',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid cyan;'
    }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_num', 'city']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid orange;'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'type': 'password',
        'style': 'border-radius: 7px; height: 45px; border: 2px solid orange;'
    }))
class contactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'type': 'text'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-input',
        'type': 'text'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'type': 'text'
    }))