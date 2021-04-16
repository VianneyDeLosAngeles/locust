from django.db import models
from datetime import datetime
import pandas as pd


class UUID_ASW(models.Model):
    tipoDocumento = models.CharField(max_length=50, help_text="Abreviacion del segmento del producto")
    factura = models.CharField(max_length=20, help_text="Nombre del segmento del producto")
    fechaFactura = models.DateTimeField(default=datetime.now, blank=True)
    UUID = models.CharField(max_length=50, help_text="UUID de la factura")
    metodoPago = models.CharField(max_length=3, help_text="Método de pago de la factura")
    usoCFDI = models.CharField(max_length=3, help_text="Uso de CFDI")
    fechaInsercion = models.DateTimeField(default=datetime.now(),blank=True) 
     

    def get_fromfile(self, excel_path):
        """Funcion para extrar la informacion del reporte de UUID del query de ASW  
        e insertarla en la base de datos. 
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
            df = pd.read_csv(excel_path, header=None, encoding = "ISO-8859-1")
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
                id_uuid=UUID_ASW.__class__.objects.create(
                        tipoDocumento = df.iloc[i,0],\
                        factura = df.iloc[i,1],\
                        fechaFactura = pd.to_datetime(df.iloc[i,2]),\
                        UUID = df.iloc[i,3],\
                        metodoPago = df.iloc[i,4],\
                        usoCFDI = df.iloc[i,5],\
                        fechaInsercion = datetime.now()
                    )
                ids.append(id_uuid)
            except Exception as e:
                #en caso de generar error se agrega a la lista el número de columma
                col_error.append(i+2) 
                print(i+2," dato: ",df.iloc[i,0])
                print("No se pudieron actualizar los datos: ",e) 
                pass  
        #si alguna columa genero error se agrega a la lista      
        if len(col_error) > 0:
            mensaje = mensaje + "No se pudieron actualizar los datos de: "+ str(col_error)

        print("mensaje: ",mensaje)
        return True,mensaje,ids