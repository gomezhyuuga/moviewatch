# -*- encoding: utf8 -*-
import django_filters
from django import forms
from django_filters.widgets import LinkWidget
from .models import Film, SlaveCatalog
from django.shortcuts import render

class FilmFilter(django_filters.FilterSet):
    genre = django_filters.AllValuesFilter(widget=LinkWidget, label='')
    name = django_filters.CharFilter(lookup_type='icontains', label='',
      widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type the movie\'s name...'}
      ))
    # director = django_filters.AllValuesFilter(widget=LinkWidget, label='Director')
    class Meta:
        model = SlaveCatalog
        fields = ['genre', 'name']
