from django.db import models
from datetime import datetime


class Interfaz(models.Model):
    fechaCarga = models.DateTimeField(default=datetime.now, blank=True)
    nombreArchivo = models.CharField(max_length=50, help_text="Nombre Archivo")
    
