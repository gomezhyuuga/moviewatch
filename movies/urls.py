from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),

  url(r'^login/$', views.login_user, name="login"),
  url(r'^logout/$', 'django.contrib.auth.views.logout',
      {'next_page': 'movies:index'}, name="logout"),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^account/$', views.account, name='account'),
  url(r'^update_rating$', views.update_rating, name='update_rating'),
  url(r'^catalog/$', views.catalog, name='catalog'),
  url(r'^catalog/(?P<film_id>[0-9]+)/$', views.detail, name='detail'),
]