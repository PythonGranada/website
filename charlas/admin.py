from django.contrib import admin
from .models import *
#Usar markdown en el administrador
from markdownx.widgets import AdminMarkdownxWidget

class NoticiaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(Noticia, NoticiaAdmin)
