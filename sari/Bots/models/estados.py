#modelo donde se define los Estados del bot 
from django.db import models
from Bots.models.modulos import Tarea 
from datetime import datetime, timezone, timedelta

class Estado(models.Model):

    estados = (
        ('Te', 'Terminado'),
        ('In', 'Iniciado'),
        ('Pr', 'Procesando'),
        ('Pa', 'Pausado'),
        ('Re', 'Reintentando'),
        ('Er', 'Error')       
    )

    descripcion = models.CharField(max_length=2, choices=estados)
    mensaje = models.CharField(max_length=100, help_text="El mensaje a mostrar al usuario", null=True )
    idTarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=True) 
    fechaInicio = models.DateTimeField(default=datetime.now,null=True) 
    fechaFin = models.DateTimeField(null=True) 
    tiempoEjecucion = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    porcentajeAvance = models.IntegerField(null=True) 



    def crear(self, descripcion, tarea, mensaje="", porcentajeAvance=0): 
        """Funcion para crear nuevos estados 
        input:
            -descripcion(String(2)): Es el estado del  bot de acuerdo a
            la siguiente lista: 
                Te  Terminado,
                In  Iniciado,
                Pr  Procesando,
                Pa  Pausado,
                Re  Reintentando,
                Er  Error 
            -tarea(String): Es un string de como es llamada la tarea de 
            acuerdo a lo registrado en la BD
            -mensaje(String): Puede recibir una cadena donde se detalle 
            lo que esta haciendo el bot. Es una opción para mostrar al 
            usuario. 
            -porcentajeAvance(int): Es un campo adicional en caso de 
            que las tareas se midan por porcentaje
        output:
            -id(int): Regresa el id del estado creado"""
        try:     
            print(datetime.now(timezone.utc))
            estado_actual= self.__class__.objects.create(descripcion = descripcion,\
                mensaje = mensaje,\
                idTarea = Tarea.objects.get(nombre=tarea),\
                fechaInicio = datetime.now(timezone.utc),\
                fechaFin = None,\
                tiempoEjecucion = None,\
                porcentajeAvance = porcentajeAvance
            )
        except Exception as e:
            estado_actual = None 
            print("Error al crear el estado: ",e) 
        return estado_actual

    def concluir(self, estado): 
        """Funcion para terminar un estado agrega la fecha final y el 
        tiempo de ejecución. 
        input:
            -estado(Objeto Estado): Es el objeto del estado a concluir
        """
        try: 
            ejecucion = (datetime.now(timezone.utc) - estado.fechaInicio) / timedelta(days=1)
            _ = self.__class__.objects.filter(id = estado.id).update(fechaFin = datetime.now(), tiempoEjecucion = ejecucion)
        except Exception as e:
            print("Error al concluir el estado: ",e) 
  
    def obtener(self, tarea, descripcion=""):
        """Funcion para obtener el ultimo estado de acuerdo al id ingresado
        o de ser necesario con el detalle de la descripción. 
        input:
            tarea(int): el id de la tarea
            descripcion(String(2)): Las dos letras que describen el estado de la tarea
        output: 
            -estado(Objeto Estado): Es el objeto del estado obtenido, en caso de que no 
            exita coincidencia el valor es None
        """
        try:
            if descripcion:
                estado = Estado.objects.filter(idTarea=tarea, descripcion=descripcion).latest('fechaInicio')
            else:
                estado = Estado.objects.filter(idTarea=tarea).latest('fechaInicio')  
        except Estado.DoesNotExist:
            print("No exiten coincidencias de la consulta")
            estado = None

        return estado    



 

