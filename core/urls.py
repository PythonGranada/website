from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

import charlas.views as charlas

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', charlas.HomeView.as_view(), name="home"),
    url(r'^markdownx/', include('markdownx.urls')),
]

#Servir static files durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
