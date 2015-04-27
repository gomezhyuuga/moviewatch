from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Film

def index(request):
  return HttpResponse("INDEX PAGE")

def catalog(request):
  film_list = Film.objects.all()
  context = { 'list': film_list }
  return render(request, "movies/catalog.html", context)

def detail(request, film_id):
  film = get_object_or_404(Film, pk=film_id)
  context = {'film': film}
  return render(request, "movies/detail.html", context)
