from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Custom admin page
class FilmAdmin(admin.ModelAdmin):
  list_display = ('name', 'director', 'genre', 'rating')
  search_fields = ['name']
  list_filter = ('director',)


admin.site.unregister(Group)
admin.site.register(Film, FilmAdmin)
admin.site.register(UserRating)
admin.site.register(Account)
admin.site.register(Country)
admin.site.register(FilmCatalog)
admin.site.register(AmericanCatalog)
admin.site.register(AsianCatalog)
admin.site.register(EuropeanCatalog)
