import os

from django.utils import timezone

from django.conf import settings
from django.shortcuts import render
#Redirects and urls
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
#ClassViews
from django.views.generic import DetailView, FormView, TemplateView, ListView
#email
from django.core.mail import send_mail
#Models and forms
from .models import Noticia, Ponente, Progreso, KungFu, Acta
from .forms import CharlaForm, ContactoForm
#external
from .github_issue import create_issue

g_token = os.environ.get("GITHUB","")


#Vista que renderiza el proximo evento fijado en las noticias
class HomeView(DetailView):
    template_name = 'home.html'
    context_object_name="event"

    def get_object(self, queryset=None):
        now = timezone.now()
        query = Noticia.objects.all()
        #Comprobar que el evento no haya pasado
        if query.count()>0: #SI hay almenos una noticia
            query = Noticia.objects.all().order_by("-fecha")[0]
            date = query.fecha
            if now >= date: #si la fecha es posterior a la del evento
                return Noticia.objects.none() #No devuelve nada
        else:
            return Noticia.objects.none() #Nada si no hay eventos

        return query #devuelve el evento si la fecha actual es anterior


#Vista para mandar charlas como issue en el repositorio
#de python-granada
class FormularioView(FormView):
    template_name = "enviar-charla.html"
    form_class = CharlaForm
    success_url = "exito"

    def form_valid(self, form):
        #Get data from form
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        titulo = form.cleaned_data['titulo']
        resumen = form.cleaned_data['resumen']

        #build email body by data provided
        subject = "Email de contacto"
        from_email = settings.EMAIL_HOST_USER
        to_list = ["yabirgb@gmail.com"]
        from_email = "me@yabirgb.com"
        #send_mail(subject, message, from_email, to_list, fail_silently=False)
        send_mail(titulo, resumen, from_email, to_list, fail_silently=False)

        create_issue(titulo,resumen)

        #Return to the success_url
        return HttpResponseRedirect(reverse_lazy(self.get_success_url()))

class NoticiaListView(ListView):
    context_object_name = 'noticias'
    model = Noticia
    page_kwarg = 'page'
    paginate_by = 10
    template_name = 'lists/noticias.html'
    ordering = "-fecha"

class NoticiaDetailView(DetailView):
    model = Noticia
    slug_field = 'slug'
    #Nombre de la variable en la url que contiene el slug
    slug_url_kwarg = 'slug'
    template_name = 'noticia.html'

class PonenteListView(ListView):
    context_object_name = 'ponentes'
    model = Ponente
    template_name = 'lists/ponentes.html'

    def grouped(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]

    def get_queryset(self):
        query = self.model.objects.all()
        queryset = self.grouped(query, 4)
        return queryset

class PonenteDetailView(DetailView):
    model = Ponente
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    template_name = 'ponente.html'
    context_object_name = "ponente"

#Manejar formulario de contacto
class ContactoFormView(FormView):
    template_name = "formularios/contacto.html"
    form_class = ContactoForm
    success_url = "exito"

    def form_valid(self, form):
        #Get data from form
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        website = form.cleaned_data['website']
        mensaje = form.cleaned_data['mensaje']

        #build email body by data provided
        subject = "Email de contacto"
        body = mensaje + "\n\n" + nombre + " - " + email + " / " + website
        from_email = settings.EMAIL_HOST_USER
        to_list = ["yabirgb@gmail.com"]
        from_email = "me@yabirgb.com"
        #send_mail(subject, message, from_email, to_list, fail_silently=False)
        send_mail(subject, body, from_email, to_list, fail_silently=False)

        #Return to the success_url
        return HttpResponseRedirect(reverse_lazy(self.get_success_url()))

class ProgresoListView(ListView):
    context_object_name = 'personas'
    model = Progreso
    template_name = 'lists/kung-fu.html'
    ordering = "-puntuacion"

class KungFuListView(ListView):
    context_object_name = 'ejercicios'
    model = KungFu
    template_name = 'lists/ejercicios.html'

    def get_object(self):
        return KungFu.objects.all().order_by("-fecha")

class ActaListView(ListView):
    context_object_name = 'actas'
    model = Acta
    template_name = 'lists/actas.html'

class ActaDetailView(DetailView):
    model = Acta
    slug_field = 'fecha'
    slug_url_kwarg = 'fecha'
    template_name = 'acta.html'

class CookiesTemplateView(TemplateView):
    template_name = 'cookies.html'

class ExitoTemplateView(TemplateView):
    template_name = 'exito.html'
