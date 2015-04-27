# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    id = models.AutoField(db_column='idAccount', primary_key=True)  # Field name made lowercase.
    country = models.ForeignKey('Country', db_column='idCountry', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=45, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    member_since = models.DateField(db_column='memberSince', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'Account'


class Catalog(models.Model):
    id = models.AutoField(db_column='idCatalog', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Catalog'


class Country(models.Model):
    id = models.AutoField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    continent = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return "%s (%s)"%(self.name, self.continent)

    class Meta:
        managed = False
        db_table = 'Country'


class Film(models.Model):
    id = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=45, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(max_length=200, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    # filepath = models.CharField(max_length=200, blank=True, null=True)
    filepath = models.FileField(upload_to='films', blank=True)
    poster = models.ImageField(upload_to='posters/%Y%m%d',blank=True)

    def poster_url(self):
        if self.poster and self.poster.url:
            return self.poster.url
        else:
            return "movies/images/no_poster.png"

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Film'


class FilmCatalog(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    film = models.ForeignKey(Film, db_column='idFilm')  # Field name made lowercase.
    catalog = models.ForeignKey(Catalog, db_column='idCatalog')  # Field name made lowercase.

    def __str__(self):
        return "%s: %s"%(self.film.name, self.catalog.name)

    class Meta:
        managed = False
        db_table = 'FilmCatalog'


class UserRating(models.Model):
    id = models.AutoField(db_column='idRating', primary_key=True)  # Field name made lowercase.
    account = models.ForeignKey(Account, db_column='idAccount')  # Field name made lowercase.
    film = models.ForeignKey(Film, db_column='idFilm')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s: %d > %s"%(self.account.username, self.rating, self.film.name)

    class Meta:
        managed = False
        db_table = 'UserRating'
