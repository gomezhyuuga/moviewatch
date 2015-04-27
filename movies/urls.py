from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^catalog/$', views.catalog, name='catalog'),
  url(r'^catalog/(?P<film_id>[0-9]+)/$', views.detail, name='detail'),
]