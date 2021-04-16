from django.db import models
from datetime import datetime


class Polizafee(models.Model):
    fechaCreacion = models.DateTimeField(default=datetime.now, blank=True)
    idVentaASW = models.CharField(max_length=3, help_text="Nombre del Area de negocio")
    idAlmacenvscentrocosto = models.CharField(max_length=100, help_text="Descripcion Marca")
    