# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmericanCatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idFilm')),
                ('name', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=45, null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, db_column='releaseDate', blank=True)),
                ('director', models.CharField(max_length=200, null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('filepath', models.FileField(upload_to='films', blank=True)),
                ('poster', models.ImageField(upload_to='posters/%Y%m%d', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'AmericanCatalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AsianCatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idFilm')),
                ('name', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=45, null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, db_column='releaseDate', blank=True)),
                ('director', models.CharField(max_length=200, null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('filepath', models.FileField(upload_to='films', blank=True)),
                ('poster', models.ImageField(upload_to='posters/%Y%m%d', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'AsianCatalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EuropeanCatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idFilm')),
                ('name', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=45, null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, db_column='releaseDate', blank=True)),
                ('director', models.CharField(max_length=200, null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('filepath', models.FileField(upload_to='films', blank=True)),
                ('poster', models.ImageField(upload_to='posters/%Y%m%d', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'EuropeanCatalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SlaveCatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idFilm')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('genre', models.CharField(max_length=45, null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, db_column='releaseDate', blank=True)),
                ('director', models.CharField(max_length=200, null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('filepath', models.FileField(upload_to='films', blank=True)),
                ('poster', models.ImageField(upload_to='posters/%Y%m%d', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'AmericanCatalog',
                'managed': False,
            },
        ),
    ]
