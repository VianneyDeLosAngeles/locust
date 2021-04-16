from django.db import models
from datetime import datetime


class SegmentoProducto(models.Model):
    segmento = models.CharField(max_length=50, help_text="Abreviacion del segmento del producto")
    descripcion = models.CharField(max_length=50, help_text="Nombre del segmento del producto")
    
    