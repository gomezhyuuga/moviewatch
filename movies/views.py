from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import Film
from .filters import FilmFilter


def index(request):
  return HttpResponse("INDEX PAGE")

def catalog(request):
  genres = Film.objects.order_by('genre').values('genre').distinct()

  film_list = Film.objects.all()
  f = FilmFilter(request.GET, queryset=Film.objects.all())
  # print(f.__dict__)
  return render_to_response('movies/catalog.html',
    {'filter': f, 'list': film_list, 'genre_list': genres})

def detail(request, film_id):
  film = get_object_or_404(Film, pk=film_id)
  context = {'film': film}
  return render(request, "movies/detail.html", context)
