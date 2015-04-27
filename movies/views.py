from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def index(request):
  return HttpResponse("INDEX PAGE")

def catalog(request):
  film_list = Film.objects.all()
  context = { 'list': film_list }
  return render(request, "movies/catalog.html", context)

def detail(request, film_id):
  return HttpResponse("DETAIL PAGE FOR %s"%film_id)
