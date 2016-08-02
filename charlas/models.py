from django.db import models
import datetime
#Librería para usar markdown
from markdownx.models import MarkdownxField
#create the SlugField
from django.utils.text import slugify
#Crop images

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

class Charla(models.Model):
    evento = models.ForeignKey(Noticia)
    documento = models.FileField(upload_to="charlas", blank = True, null = True)
    url = models.URLField(blank=True, null=True)
    nombre = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre

class Ponente(models.Model):
    nombre = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="ponentes/profile")
    contact = models.EmailField(blank=True, null=True)
    charlas = models.ManyToManyField(Charla, blank=True, null=True)
    twitter = models.CharField(blank=True, null=True, max_length=100)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    linkedin = models.CharField(blank=True, null=True, max_length=100)
    website = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.nombre
