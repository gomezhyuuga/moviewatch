# from django.forms import TextInput, PasswordInput, EmailInput, Select
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account
from django.forms import ModelForm
from django import forms

class AccountForm(ModelForm):
  class Meta:
    model = Account
    fields = ['firstname', 'lastname', 'country']
    widgets = {
      'firstname': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'John'}),
      'lastname': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'Doe'}),
      'country': Select(attrs={
        'class': 'form-control input-lg'}),
    }

class UserSettingsForm(ModelForm):
  email = forms.EmailField(required=True,
    widget=EmailInput(attrs={
            'class': 'form-control input-lg',
            'autocomplete': 'off',
            'required': 'required',
            'placeholder': 'best@moviewatch.com'}))
  password1 = forms.CharField(label="Password",
        widget=PasswordInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': '******'}))
  password2 = forms.CharField(label="Password confirmation",
        widget=PasswordInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': '******'}))
  class Meta:
    model = User
    fields = ['email']

class AccountSettingsForm(ModelForm):
  class Meta:
    model = Account
    fields = ['firstname', 'lastname']
    widgets = {
      'firstname': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'John'}),
      'lastname': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'Doe'})
    }

class SignupForm(UserCreationForm):
  email = forms.EmailField(required=True,
    widget=EmailInput(attrs={
            'class': 'form-control input-lg',
            'autocomplete': 'off',
            'required': 'required',
            'placeholder': 'best@moviewatch.com'}))
  password1 = forms.CharField(label="Password",
        widget=PasswordInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': '******'}))
  password2 = forms.CharField(label="Password confirmation",
        widget=PasswordInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': '******'}))
  class Meta:
    model = User
    fields = ['username', 'email']
    widgets = {
      'username': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'Username'}),
    }