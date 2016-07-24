from django.shortcuts import render
#Models and forms
from .models import Noticia
from .forms import CharlaForm
#Redirects and urls
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
#ClassViews
from django.views.generic import DetailView, FormView, TemplateView
#external
from .github_issue import create_issue


#Vista que renderiza el proximo evento fijado en las noticias
class HomeView(DetailView):
    template_name = 'home.html'
    context_object_name="event"

    def get_object(self, queryset=None):
        return Noticia.objects.all().last()

#Vista para mandar charlas como issue en el repositorio
#de python-granada
class FormularioView(FormView):
    template_name = "enviar-charla.html"
    form_class = CharlaForm
    success_url = "home"

    def form_valid(self, form):
        #Get data from form
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        titulo = form.cleaned_data['titulo']
        resumen = form.cleaned_data['resumen']

        #build the issue body from the data provided
        body = resumen + "\n\n" + nombre + " - " + email
        create_issue(titulo, body)

        return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
