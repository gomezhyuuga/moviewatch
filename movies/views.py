from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from .models import Film
from .filters import FilmFilter
from django.contrib.auth import logout, authenticate, login
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

from .forms import AccountForm, SignupForm

def index(request):
  c = RequestContext(request)
  return render_to_response('movies/index.html', c)

def signup(request):
  c = RequestContext(request)
  a_form = AccountForm(request.POST)
  u_form = SignupForm(request.POST)
  c.push({'account_form': a_form, 'user_form': u_form})
  
  if request.method == 'GET':
    return render_to_response('movies/signup.html', c)
  elif request.method == 'POST':
    if a_form.is_valid() and u_form.is_valid():
      account = a_form.save(commit=False)
      user = u_form.save()
      user.first_name = account.firstname
      user.last_name = account.lastname
      account.user = user
      account.username = user.username
      account.email = user.email
      account.password = user.password
      account.save()
      user.save()

      # Redirect to a success page.
      return redirect('movies:catalog')
    else:
      return render_to_response('movies/signup.html', c)

def login_user(request):
  c = RequestContext(request)
  if request.user.is_authenticated():
    return redirect('movies:catalog')
  if request.method == 'GET':
    return render_to_response('movies/login.html', c)
  elif request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
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
  c = RequestContext(request)
  if not request.user.is_authenticated():
    return redirect('movies:login')

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
