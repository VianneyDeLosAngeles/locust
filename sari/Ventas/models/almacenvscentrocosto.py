from django.db import models
import pandas as pd

class Almacencentrocosto(models.Model):
    almacenASW = models.CharField(max_length=3, help_text="Id del alamcen en ASW")
    centroCostosSAP = models.CharField(max_length=8, help_text="Id del Centro de Costos e  SAP")
    descripcioncentroCostos = models.CharField(max_length=100, help_text="Nombre del Centro de Costos")
    

    def get_fromfile(self, excel_path):

        """Funcion para extrar la informacion del un archivo excel 
        input:
            excel_path(String): Es una cadena que incluye la direccion y nombre del archivo
        output: 
            -(booleano):
            -mensaje(String): En caso de realizar el insert concluido, de lo contrario se 
            incluye un texto con el error capturado 
        """
        mensaje = ""
        #abro el archivo, en caso de generar error termina ejecuta el return 
        try: 
            df = pd.read_excel(excel_path, sheet_name=0, header=0)
        except Exception as e:
            mensaje = 'No se pudo abrir el archivo, error: ' + str(e)
            return False,mensaje
        #lista con el numero de la columna de excel que dio error     
        col_error = []
        #lista con los id's de los insert de las ventas
        i=0
        #se realiza el insert de las ventas 
        for i in range(df.shape[i]):
            try:  
                _, _ = self.__class__.objects.update_or_create(almacenASW=str(df.iloc[i,0]),\
                        defaults={
                            'centroCostosSAP': df.iloc[i,1],\
                            'descripcioncentroCostos': df.iloc[i,2],\
                        })


            except Exception as e:
                #en caso de generar error se agrega a la lista el número de columma
                col_error.append(i+2) 
                print("No se pudieron actualizar los datos ",e) 
                pass  
        #si alguna columa genero error se agrega a la lista      
        if len(col_error) > 0:
            mensaje = mensaje + "No se pudieron actualizar los datos de: "+ str(col_error)

        print("mensaje: ",mensaje)
        return True,mensaje    




