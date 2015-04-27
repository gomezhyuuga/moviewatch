from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('movies.urls', namespace='movies')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
