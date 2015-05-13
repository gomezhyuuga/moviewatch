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

from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete


from django.db import models

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
    def film_url(self):
        if self.filepath and self.filepath.url:
            return self.filepath.url
        else:
            return "/media/films/no_film.webm"

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Film'
        ordering = ['name']

class SlaveCatalog(models.Model):
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
    def film_url(self):
        if self.filepath and self.filepath.url:
            return self.filepath.url
        else:
            return "/media/films/no_film.webm"

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = settings.FILM_CATALOG
        ordering = ['name']


class Account(models.Model):
    id = models.AutoField(db_column='idAccount', primary_key=True)  # Field name made lowercase.
    country = models.ForeignKey('Country', db_column='idCountry', blank=False)  # Field name made lowercase.
    username = models.CharField(max_length=45, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=False)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=False)  # Field name made lowercase.
    email = models.CharField(max_length=45, blank=False)
    address = models.CharField(max_length=45, blank=True, null=True)
    member_since = models.DateField(db_column='memberSince', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True)

    user = models.OneToOneField(User)

    def __str__(self):
        if (self.username):
            return self.username
        return 'no_user'

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



class UserRating(models.Model):
    id = models.AutoField(db_column='idRating', primary_key=True)  # Field name made lowercase.
    account = models.ForeignKey(Account, db_column='idAccount')  # Field name made lowercase.
    film = models.ForeignKey(Film, db_column='idFilm')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if not self.account or not self.film:
            return "Invalid"
        return "%s: %d > %s"%(self.account.username, self.rating, self.film.name)

    class Meta:
        managed = False
        unique_together = ("account", "film")
        db_table = 'UserRating'


class AmericanCatalog(models.Model):
    id = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=False, null=True)
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
    def film_url(self):
        if self.filepath and self.filepath.url:
            return self.filepath.url
        else:
            return "/media/films/no_film.webm"

    def __str__(self):
        if not self.name:
            return "No name"
        return self.name

    class Meta:
        managed = False
        db_table = 'AmericanCatalog'
        ordering = ['name']



class AsianCatalog(models.Model):
    id = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=False, null=True)
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
    def film_url(self):
        if self.filepath and self.filepath.url:
            return self.filepath.url
        else:
            return "/media/films/no_film.webm"

    def __str__(self):
        if not self.name:
            return "No name"
        return self.name

    class Meta:
        managed = False
        db_table = 'AsianCatalog'
        ordering = ['name']



class EuropeanCatalog(models.Model):
    id = models.AutoField(db_column='idFilm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=False, null=True)
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
    def film_url(self):
        if self.filepath and self.filepath.url:
            return self.filepath.url
        else:
            return "/media/films/no_film.webm"

    def __str__(self):
        if not self.name:
            return "No name"
        return self.name

    class Meta:
        managed = False
        db_table = 'EuropeanCatalog'
        ordering = ['name']


class FilmCatalog(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    film = models.ForeignKey(Film, db_column='idFilm')  # Field name made lowercase.
    catalog = models.ForeignKey(Catalog, db_column='idCatalog')  # Field name made lowercase.

    def __str__(self):
        return "%s: %s"%(self.film.name, self.catalog.name)

    class Meta:
        managed = False
        db_table = 'FilmCatalog'

# def copy_account(sender, instance, **kwargs):
#     if instance.catalog.id == 1:
#         copy = AmericanCatalog()
#     elif instance.catalog.id == 2:
#         copy = EuropeanCatalog()
#     else:
#         copy = AsianCatalog()

def copy_film(sender, instance, **kwargs):
    print("Diplicating... ")
    print(instance)
    if instance.catalog.id == 1:
        copy = AmericanCatalog()
    elif instance.catalog.id == 2:
        copy = EuropeanCatalog()
    else:
        copy = AsianCatalog()
    film = instance.film
    copy.id = film.id
    copy.name = film.name
    copy.genre = film.genre
    copy.rating = film.rating
    copy.description = film.description
    copy.releasedate = film.releasedate
    copy.director = film.director
    copy.duration = film.duration
    copy.filepath = film.filepath
    copy.poster = film.poster
    copy.save()
    print("SAVED COPY OF: ")
    print(copy)

def post_delete_film(sender, instance, **kwargs):
    try:
        if instance.catalog.id == 1:
            f = AmericanCatalog.objects.get(pk=instance.film.id)
        elif instance.catalog.id == 2:
            f = EuropeanCatalog.objects.get(pk=instance.film.id)
        else:
            f = AsianCatalog.objects.get(pk=instance.film.id)
        f.delete()
        print("DELETED FILM FROM CATALOG")
    except ObjectDoesNotExist:
        pass

post_save.connect(copy_film, sender=FilmCatalog, dispatch_uid="duplicate_film_in_catalog")
post_delete.connect(post_delete_film, sender=FilmCatalog, dispatch_uid="delete_film_in_catalog")