import charlas.views as charlas
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', charlas.HomeView.as_view(), name="home"),
    url(r'^enviar/$', charlas.FormularioView.as_view(), name="enviar"),
    url(r'^noticias/$', charlas.NoticiaListView.as_view(), name="noticias"),
    url(r'^noticias/(?P<slug>[\w-]+)$', charlas.NoticiaDetailView.as_view(), name="ndetail"),
    url(r'^ponentes/$', charlas.PonenteListView.as_view(), name="ponentes"),
    url(r'^ponentes/(?P<pk>\d+)$', charlas.PonenteDetailView.as_view(), name ="ponente"),
    url(r'^contacto/$', charlas.ContactoFormView.as_view(), name="contacto"),
    url(r'kung-fu/$', charlas.ProgresoListView.as_view(), name = "kung-fu"),
    url(r'ejercicios/$', charlas.KungFuListView.as_view(), name = "ejercicios"),
    url(r'^actas/$', charlas.ActaListView.as_view(), name="actas"),
    url(r'^actas/(?P<fecha>[\w-]+)$', charlas.ActaDetailView.as_view(), name="acta"),
]
