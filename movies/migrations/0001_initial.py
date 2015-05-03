# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idAccount')),
                ('username', models.CharField(null=True, blank=True, max_length=45)),
                ('firstname', models.CharField(null=True, blank=True, max_length=45, db_column='firstName')),
                ('lastname', models.CharField(null=True, blank=True, max_length=45, db_column='lastName')),
                ('email', models.CharField(null=True, blank=True, max_length=45)),
                ('address', models.CharField(null=True, blank=True, max_length=45)),
                ('member_since', models.DateField(null=True, blank=True, db_column='memberSince')),
                ('password', models.CharField(null=True, blank=True, max_length=45)),
            ],
            options={
                'db_table': 'Account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idCatalog')),
                ('name', models.CharField(null=True, blank=True, max_length=45)),
            ],
            options={
                'db_table': 'Catalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idCountry')),
                ('name', models.CharField(null=True, blank=True, max_length=45)),
                ('continent', models.CharField(null=True, blank=True, max_length=45)),
            ],
            options={
                'db_table': 'Country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idFilm')),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('genre', models.CharField(null=True, blank=True, max_length=45)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('releasedate', models.DateField(null=True, blank=True, db_column='releaseDate')),
                ('director', models.CharField(null=True, blank=True, max_length=200)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('filepath', models.FileField(blank=True, upload_to='films')),
                ('poster', models.ImageField(blank=True, upload_to='posters/%Y%m%d')),
            ],
            options={
                'db_table': 'Film',
                'managed': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FilmCatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='id')),
            ],
            options={
                'db_table': 'FilmCatalog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='idRating')),
                ('rating', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'UserRating',
                'managed': False,
            },
        ),
    ]
