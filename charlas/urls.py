import charlas.views as charlas
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', charlas.HomeView.as_view(), name="home"),
    url(r'^enviar/$', charlas.FormularioView.as_view(), name="enviar"),
    url(r'^noticias/$', charlas.NoticiaListView.as_view(), name="noticias"),
    url(r'^noticias/(?P<slug>[\w-]+)$', charlas.NoticiaDetailView.as_view(), name="ndetail"),
]
