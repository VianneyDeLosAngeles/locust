from django.db import models
from datetime import datetime
from Ventas.models.marcavsareanegocio import Marcaarea 


class Cuadre(models.Model):

    fuente = (
    ('R', 'Retail'),
    ('W', 'Wholesale')
    )


    idMarca = models.ForeignKey(Marcaarea, on_delete=models.CASCADE)
    canal = models.CharField(max_length=8, help_text="Nombre del canal")
    totalASW = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=False)
    totalSAP = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=False)
    fechaCreacion = models.DateTimeField(default=datetime.now, blank=True)
    factura = models.CharField(max_length=8, help_text="Nombre del canal")
    fuente = models.CharField(max_length=1, choices=fuente)


