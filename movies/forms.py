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

class SignupForm(UserCreationForm):
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
    fields = ['username']
    widgets = {
      'username': TextInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'Username'}),
      'email': EmailInput(attrs={
        'class': 'form-control input-lg',
        'autocomplete': 'off',
        'placeholder': 'best@moviewatch.com'}),
    }