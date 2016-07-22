from django.db import models
import datetime
#Librería para usar markdown
from markdownx.models import MarkdownxField

# Create your models here.
class Noticia(models.Model):
    nombre = models.CharField(blank=True, max_length=250)
    fecha = models.DateTimeField(blank=True, default=datetime.datetime.now)
    cuerpo = MarkdownxField()

    def __str__(self):
        return self.nombre
