from django.contrib import admin
from .models import *

# Custom admin page
class FilmAdmin(admin.ModelAdmin):
  search_fields = ['name']
  list_filter = ('director',)


admin.site.register(Film, FilmAdmin)
admin.site.register(UserRating)
admin.site.register(Account)
admin.site.register(Country)
admin.site.register(FilmCatalog)
