import json
import os

from django.core.management.base import BaseCommand, CommandError
from charlas.models import Progreso
from django.conf import settings

class Command(BaseCommand):
    help = 'Populates data from json file'


    def handle(self, *args, **options):
        jfile = os.path.join(settings.BASE_DIR, "populate_data/usuarios.json")
        with open(jfile, encoding='utf-8') as data_file:
            data = json.load(data_file)
            for user in data:
                d = Progreso(nombre = user["usuario"], puntuacion = user["puntuacion"])
                d.save()

        print("Task completed")
