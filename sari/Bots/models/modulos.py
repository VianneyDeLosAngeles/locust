from django.db import models
import os 

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


class Modulo(models.Model):
    
    nombre = models.CharField(max_length=50, help_text="Nombre del modulo")
    submodulo = models.CharField(max_length=50, help_text="Nombre del submodulo", null=True)


class Tarea(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del modulo")
    idModulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, null=True)
    


        
               