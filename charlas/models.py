from django.db import models
import datetime
#Librería para usar markdown
from markdownx.models import MarkdownxField
#create the SlugField
from django.utils.text import slugify

# Create your models here.
class Noticia(models.Model):
    nombre = models.CharField(blank=True, max_length=250)
    slug = models.SlugField(blank = True)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.now)
    cuerpo = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Noticia, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
