from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from charlas.views import CookiesTemplateView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('charlas.urls'), name="home"),
    url(r'^cookies/', CookiesTemplateView.as_view() , name="cookies"),
    #url(r'^gallery/', include('gallery.urls'), name="gallery"),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),
]

#Servir static files durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
