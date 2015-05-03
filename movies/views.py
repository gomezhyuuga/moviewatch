from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from .models import Film
from .filters import FilmFilter
from django.contrib.auth import logout, authenticate, login
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .forms import SignupForm

def index(request):
  return HttpResponse("INDEX PAGE")

def signup(request):
  c = RequestContext(request)
  form = SignupForm
  c.push({'form': form})

  return render_to_response('movies/signup.html', c)

def login_user(request):
  if request.method == 'GET':
    c = RequestContext(request)
    return render_to_response('movies/login.html', c)
  elif request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    c = RequestContext(request)
    if user is not None:
      if user.is_active:
        # Redirect to a success page.
        login(request, user)
        return redirect('movies:catalog')
      else:
      # Return a 'disabled account' error message
        c.push( { 'errors': ('Disabled user') } )
    else:
      # Return an 'invalid login' error message.
      c.push( { 'errors': ('Invalid user/password') } )
    return render_to_response('movies/login.html', c)

def logout(request):
  logout(request, current_app="movies", next_page="movies:index")
  # return redirect(reverse('movies:index'))

def catalog(request):
  genres = Film.objects.order_by('genre').values('genre').distinct()

  context = RequestContext(request)

  film_list = Film.objects.all()
  f = FilmFilter(request.GET, queryset=Film.objects.all())
  # print(f.__dict__)
  context.push( {'filter': f, 'list': film_list, 'genre_list': genres} )
  return render_to_response('movies/catalog.html', context)

def detail(request, film_id):
  film = get_object_or_404(Film, pk=film_id)
  context = {'film': film}
  return render(request, "movies/detail.html", context)
