import json
import os

from django.core.management.base import BaseCommand, CommandError
from charlas.models import KungFu
from django.conf import settings

class Command(BaseCommand):
    help = 'Populates data from json file'


    def handle(self, *args, **options):
        jfile = os.path.join(settings.BASE_DIR, "populate_data/ejercicios.json")
        with open(jfile, encoding='utf-8') as data_file:
            data = json.load(data_file)
            for ejercicio in data:
                d = KungFu(nombre = ejercicio["name"], descripcion = ejercicio["description"], enlace = ejercicio["url"], fecha = ejercicio["date"])
                d.save()

        print("Task completed")
