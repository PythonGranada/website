from django.shortcuts import render
from .models import Noticia

# Create your views here.
from django.views.generic import DetailView

class HomeView(DetailView):
    template_name = 'home.html'
    context_object_name="event"

    def get_object(self, queryset=None):
        return Noticia.objects.all().last()
