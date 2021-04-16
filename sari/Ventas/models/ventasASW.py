

import xlrd
import pandas as pd
from django.db import models
from datetime import datetime
from Ventas.models.marcavsareanegocio import Marcaarea 
from Ventas.models.almacenvscentrocosto import Almacencentrocosto


class ventasASW(models.Model):

    CARGO = (
    ('Y', 'Si'),
    ('N', 'No')
    )

    marca = models.ForeignKey(Marcaarea, on_delete=models.CASCADE)
    #idAlmacen = models.ForeignKey(Almacencentrocosto, on_delete=models.CASCADE) 
    idAlmacen = models.CharField(max_length=5, help_text="Bodega")   
    grupo = models.CharField(max_length=5, help_text="Grupo")
    cliente = models.CharField(max_length=100, help_text="Descripción del cliente")
    nombreCliente = models.CharField(max_length=100, help_text="Tipo de documento")
    fechaFactura = models.DateTimeField( blank=True) 
    factura = models.CharField(max_length=20, help_text="No de Factura")
    tipoFactura2NC = models.IntegerField(null=True)
    producto = models.CharField(max_length=10, help_text="Clave del producto")
    #descripcion = models.CharField(max_length=100, help_text="Descripción del producto", null=True)
    descuento = models.CharField(max_length=150, help_text="Descripcion del descuento")
    pedido = models.CharField(max_length=10, help_text="Bodega")
    valorNeto = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad = models.IntegerField(null=True)
    grupoCuenta = models.CharField(max_length=2, help_text="Grupo de la cuenta")
    categoriaProducto1 = models.CharField(max_length=5, help_text="Categoria del producto 1", null=True)
    descripcionCategoria1 = models.CharField(max_length=100, help_text="Categoria del producto 1", null=True)
    categoriaProducto2 = models.CharField(max_length=5, help_text="Categoria del producto 2", null=True)
    categoriaProducto3 = models.CharField(max_length=5, help_text="Categoria del producto 3", null=True)
    categoriaProducto4 = models.CharField(max_length=5, help_text="Categoria del producto 4", null=True)
    categoriaProducto5 = models.CharField(max_length=5, help_text="Categoria del producto 5", null=True)
    categoriaPodructo6 = models.CharField(max_length=5, help_text="Categoria del producto 6")
    tipoOrden = models.IntegerField(null=True)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    periodoContable = models.DateField(blank=True)
    libreCargo = models.CharField(max_length=1, choices=CARGO, null=True)
    fechaInsercion = models.DateTimeField(default=datetime.now(), blank=True)    



    def get_fromfile(self, excel_path):
        """Funcion para extrar la informacion del reporte de SAP FBL3N y cargarla 
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
            #xl = xlrd.open_workbook(excel_path, encoding_override="utf-8")
        
            #me paso a movimientos EMA
            #ws = xl.sheet_by_index(1)
            df = pd.read_csv(excel_path, encoding = "ISO-8859-1", header=None)
        except Exception as e:
            mensaje = 'No se pudo abrir el archivo, error: ' + str(e)
            print(mensaje)
            #return False,mensaje
            pass
        #lista con el numero de la columna de excel que dio error     
        col_error = []
        #lista con los id's de los insert de las ventas
        ids_ventas = []
        i=0
        #se realiza el insert de las ventas 
        for i in range(df.shape[i]):
            try: 
                periodo = str(df.iloc[i,23])+"01"
                print("marca: ",df.iloc[i,0], " libre: ", periodo )
                #print(periodo.astype('datetime64[ns]'))
                print( pd.to_datetime(periodo) )


                idMarca = Marcaarea.objects.get(marcaASW = str(df.iloc[i,0]))
                #idAlmacen = Almacencentrocosto.objects.get(almacenASW = df.iloc[i,1])
                id_venta=self.__class__.objects.create(
                        marca = idMarca,\
                        idAlmacen = df.iloc[i,1],\
                        grupo = df.iloc[i,2],\
                        cliente = df.iloc[i,3],\
                        nombreCliente = df.iloc[i,4],\
                        fechaFactura = pd.to_datetime(df.iloc[i,5]),\
                        factura = df.iloc[i,6],\
                        tipoFactura2NC = df.iloc[i,7],\
                        producto = df.iloc[i,8],\
                        descuento = df.iloc[i,9],\
                        pedido = df.iloc[i,10],\
                        valorNeto = df.iloc[i,11],\
                        cantidad = df.iloc[i,12],\
                        grupoCuenta = df.iloc[i,13],\
                        categoriaProducto1 = df.iloc[i,14],\
                        descripcionCategoria1 = df.iloc[i,15],\
                        categoriaProducto2 = df.iloc[i,16],\
                        categoriaProducto3 = df.iloc[i,17],\
                        categoriaProducto4 = df.iloc[i,18],\
                        categoriaProducto5 = df.iloc[i,19],\
                        categoriaPodructo6 = df.iloc[i,20],\
                        tipoOrden = df.iloc[i,21],\
                        costo = df.iloc[i,22],\
                        periodoContable = datetime.strptime(periodo, '%Y%m%d'),\
                        libreCargo = str(df.iloc[i,24]),\
                        fechaInsercion = datetime.now()
                    )
                ids_ventas.append(id_venta)

            except Marcaarea.DoesNotExist:
                print("La marca que intenta insertar no esta registrada, col: " + str(i+2) )
                mensaje = "La marca que intenta insertar no esta registrada, col: " + str(i+2)
                return False,mensaje,ids_ventas               
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
        return True,mensaje,ids_ventas 
