import pandas as pd
from django.db import models
from datetime import datetime
from Ventas.models.marcavsareanegocio import Marcaarea 


class Descuento(models.Model):

    parteCuenta1 = models.CharField(max_length=5, help_text="Parte de la cuenta 1")
    parteCuenta2 = models.CharField(max_length=5, help_text="Parte de la cuenta 2")
    parteCuenta3 = models.CharField(max_length=5, help_text="Parte de la cuenta 3")
    factura = models.CharField(max_length=20, help_text="No de Factura")
    peridodContable = models.DateTimeField(default=datetime.now, blank=True)
    journalNumber = models.CharField(max_length=8, help_text="Nombre del canal")
    monedaTransaccion = models.CharField(max_length=3, help_text="Moneda de transaccion")  
    montoMonedasistema = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=False)
    montoMonedatransaccion = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=False)
    descripcion = models.CharField(max_length=100, help_text="Descripción del descuento")
    tipo = models.CharField(max_length=3, help_text="Tipo de descuento")
    cantidad = models.IntegerField(null=True)
    fechaFactura = models.DateTimeField(blank=True) 
    fechaInsercion = models.DateTimeField(default=datetime.now(),blank=True) 

    def get_fromfile(self, excel_path):
        """Funcion para extrar la informacion de descuentos del query de ASW e insertar la info
        en la base de datos. Actualmente usada en el área de Wholesale. 
        input:
            excel_path(String): Es una cadena que incluye la direccion y nombre del archivo
        output: 
            -(booleano):
            -mensaje(String): En caso de realizar el insert concluido, de lo contrario se 
            incluye un texto con el error capturado 
            -lista(int): Regresa una lista con los id's de las ventas insertadas
        """
        mensaje = ""
        #abro el archivo, en caso de generar error termina ejecuta el return 
        try: 
            df = pd.read_csv(excel_path, encoding = "ISO-8859-1", header=None)
        except Exception as e:
            mensaje = 'No se pudo abrir el archivo, error: ' + e
            return False,mensaje
        #lista con el numero de la columna de excel que dio error     
        col_error = []
        #lista con los id's de los insert de las ventas
        ids = []
        i=0
        #se realiza el insert de las ventas 
        for i in range(df.shape[i]-1):
            try: 
                periodo = str(df.iloc[i,4])+"01"  
                id_descuento=self.__class__.objects.create(
                        parteCuenta1 = df.iloc[i,0],\
                        parteCuenta2 = df.iloc[i,1],\
                        parteCuenta3 = df.iloc[i,2],\
                        factura = df.iloc[i,3],\
                        peridodContable = datetime.strptime(periodo, '%Y%m%d'),\
                        journalNumber = df.iloc[i,5],\
                        monedaTransaccion = df.iloc[i,6],\
                        montoMonedasistema = df.iloc[i,7],\
                        montoMonedatransaccion = df.iloc[i,8],\
                        descripcion = df.iloc[i,9],\
                        tipo = df.iloc[i,10],\
                        cantidad = df.iloc[i,11],\
                        fechaFactura = pd.to_datetime(df.iloc[i,12]),\
                        fechaInsercion = datetime.now()
                    )
                ids.append(id_descuento)
            except Exception as e:
                #en caso de generar error se agrega a la lista el número de columma
                col_error.append(i+2) 
                print(i+2," dato: ",df.iloc[i,0])
                print("No se pudieron actualizar los datos: ",a) 
                pass  
        #si alguna columa genero error se agrega a la lista      
        if len(col_error) > 0:
            mensaje = mensaje + "No se pudieron actualizar los datos de: "+ str(col_error)

        print("mensaje: ",mensaje)
        return True,mensaje,ids