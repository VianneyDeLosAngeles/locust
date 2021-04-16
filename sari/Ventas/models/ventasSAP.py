from django.db import models
import pandas as pd
from datetime import datetime 

class ventasSAP(models.Model):

    FUENTE_DES = (
    ('R', 'Retail'),
    ('W', 'Wholesale')
    )


    numeroDocumento = models.IntegerField(null=True)
    tipoDocumento = models.CharField(max_length=8, help_text="Tipo de documento")
    fechaDocumento = models.DateTimeField( blank=True)
    fechaPosteo = models.DateTimeField( blank=True, null=True)
    periodoPosteo = models.IntegerField(null=True)
    llavePosteo = models.IntegerField(null=True)
    codigoTax = models.CharField(max_length=3, help_text="Codigo Tax")
    montoMonedadocumento = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    moneda = models.CharField(max_length=3, help_text="Moneda")
    montoMonedasistema = models.DecimalField(max_digits=12, decimal_places=2)
    areaNegocio = models.CharField(max_length=3, help_text="Area de negocio ")
    centroCostos = models.CharField(max_length=10, help_text="Centro de costos")
    descripcionCentrocostos = models.CharField(max_length=100, help_text="Descripcion del centro de costos")
    descripcionCuentacontable = models.CharField(max_length=100, help_text="Descripción Cuenta Contable")
    referenciaFactura = models.CharField(max_length=20, help_text="Referencia de la Factura")
    cuentaContable = models.CharField(max_length=100, help_text="Cuenta Contable",null=True)
    especialGL = models.CharField(max_length=100, help_text="Especial GL",null=True)
    monedaLocal = models.CharField(max_length=5, help_text="Moneda Local",null=True)
    documentoCompensacion = models.CharField(max_length=20, help_text="Moneda Local", null=True)
    cliente = models.IntegerField(null=True) 
    metodoPago = models.IntegerField(null=True)
    texto = models.CharField(max_length=200, help_text="Texto",null=True)
    textoExistente = models.CharField(max_length=200, help_text="Texto Existente", null=True)
    bloqueoPago = models.CharField(max_length=100, help_text="Bloqueo de pago", null=True)
    fechaVencimiento = models.DateTimeField(blank=True, null=True) 
    fuente = models.CharField(max_length=1, choices=FUENTE_DES, null=True)
    fechaInsercion = models.DateTimeField(default=datetime.now(), blank=True)



    def get_fromfileFBL3N(self, excel_path):
        """Funcion para extrar la informacion del reporte de SAP FBL3N y cargarla 
        en la base de datos. Actualmente usada en el área de Retail. 
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
            df = pd.read_excel(excel_path, sheet_name=0, header=0)
        except Exception as e:
            mensaje = 'No se pudo abrir el archivo, error: ' + str(e)
            return False,mensaje
        #lista con el numero de la columna de excel que dio error     
        col_error = []
        #lista con los id's de los insert de las ventas
        ids_ventas = []
        i=0
        #se realiza el insert de las ventas 
        for i in range(df.shape[i]-1):
            try:  
                id_venta=self.__class__.objects.create(
                        numeroDocumento = int(df.iloc[i,1]),\
                        tipoDocumento = df.iloc[i,2],\
                        fechaDocumento = pd.to_datetime(df.iloc[i,3]),\
                        fechaPosteo = pd.to_datetime(df.iloc[i,4]),\
                        periodoPosteo = int(df.iloc[i,5]),\
                        llavePosteo = int(df.iloc[i,6]),\
                        codigoTax = df.iloc[i,7],\
                        montoMonedadocumento = float(df.iloc[i,8]),\
                        moneda = df.iloc[i,9],\
                        montoMonedasistema = float(df.iloc[i,10]),\
                        areaNegocio = df.iloc[i,11],\
                        centroCostos = df.iloc[i,15],\
                        descripcionCentrocostos = df.iloc[i,11],\
                        descripcionCuentacontable = df.iloc[i,18],\
                        referenciaFactura = df.iloc[i,19],\
                        cuentaContable = df.iloc[i,20],\
                        fuente = "R",\
                        fechaInsercion = datetime.now()
                    )
                ids_ventas.append(id_venta)
            except Exception as e:
                #en caso de generar error se agrega a la lista el número de columma
                col_error.append(i+2) 
                print("No se pudieron actualizar los datos ",e) 
                pass  
        #si alguna columa genero error se agrega a la lista      
        if len(col_error) > 0:
            mensaje = mensaje + "No se pudieron actualizar los datos de: "+ str(col_error)

        print("mensaje: ",mensaje)
        return True,mensaje,ids_ventas    

    def get_fromfileFBL5N(self, excel_path):
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
            df = pd.read_excel(excel_path, sheet_name=0, header=1)
        except Exception as e:
            mensaje = 'No se pudo abrir el archivo, error: ' + str(e)
            return False,mensaje
        #lista con el numero de la columna de excel que dio error     
        col_error = []
        #lista con los id's de los insert de las ventas
        ids_ventas = []
        i=0
        #se realiza el insert de las ventas 
        for i in range(df.shape[i]-1):
            try:  
                id_venta=self.__class__.objects.create(
                        numeroDocumento = int(df.iloc[i,0]),\
                        tipoDocumento = df.iloc[i,1],\
                        fechaDocumento = pd.to_datetime(df.iloc[i,2]),\
                        especialGL = pd.to_datetime(df.iloc[i,3]),\
                        montoMonedasistema = float(df.iloc[i,4]),\
                        monedaLocal = df.iloc[i,5],\
                        documentoCompensacion = df.iloc[i,6],\
                        texto = df.iloc[i,7],\
                        referenciaFactura = df.iloc[i,8],\
                        moneda = df.iloc[i,9],\
                        areaNegocio = df.iloc[i,10],\
                        cliente = df.iloc[i,11],\
                        cuentaContable = df.iloc[i,12],\
                        metodoPago = df.iloc[i,13],\
                        textoExistente = df.iloc[i,14],\
                        bloqueoPago = df.iloc[i,15],\
                        fechaVencimiento = pd.to_datetime(df.iloc[i,16]),\
                        fuente = "W",\
                        fechaInsercion = datetime.now()
                    )
                ids_ventas.append(id_venta)
            except Exception as e:
                #en caso de generar error se agrega a la lista el número de columma
                col_error.append(i+2) 
                print(i+2," dato: ",df.iloc[i,0])
                print("No se pudieron actualizar los datos: ",str(e)) 
                pass  
        #si alguna columa genero error se agrega a la lista      
        if len(col_error) > 0:
            mensaje = mensaje + "No se pudieron actualizar los datos de: "+ str(col_error)

        print("mensaje: ",mensaje)
        return True,mensaje,ids_ventas 


