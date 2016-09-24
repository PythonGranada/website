from django.contrib import admin
from .models import *
#Usar markdown en el administrador
from markdownx.widgets import AdminMarkdownxWidget

#Crop images in admin

#Render the markdown on the admin panel
class NoticiaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }



admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Ponente)
admin.site.register(Charla)
admin.site.register(KungFu)
admin.site.register(Progreso)
admin.site.register(Acta)
