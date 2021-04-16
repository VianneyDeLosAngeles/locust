from django.db import models



class Marcaarea(models.Model):
    marcaASW = models.CharField(max_length=3, help_text="Nombre de la Marca")
    areanegocioSAP = models.CharField(max_length=3, help_text="Nombre del Area de negocio")
    descripcionMarca = models.CharField(max_length=100, help_text="Descripcion Marca")
    
