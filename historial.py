import json
import datetime

class Historial:
    def __init__(self):
        self.transacciones = []
        self.__codigo_cuenta = None
        self.__tipo_transaccion = None
        self.__fecha = None

    # Geters
    def get_codigo_cuenta(self):
        return self.__codigo_cuenta
    
    def get_tipo_transaccion(self):
        return self.__tipo_transaccion

    def get_fecha(self):
        return self.__fecha
    
    # Seters
    def set_codigo_cuenta(self, codigo_cuenta):
        self.__codigo_cuenta = codigo_cuenta

    def set_tipo_transaccion(self, tipo_transaccion):
        self.__tipo_transaccion = tipo_transaccion

    def set_fecha(self, fecha):
        self.__fecha = fecha

    # Metodo str
    def __str__(self):
        return f"Código de cuenta: {self.__codigo_cuenta}, Tipo de transacción: {self.__tipo_transaccion}, Fecha: {self.__fecha}"
    
    # Metodos de la Clase        
    def agregar_transaccion(self):
        transaccion = {
            'codigo_cuenta': self.__codigo_cuenta,
            'tipo_transaccion': self.__tipo_transaccion,
            'fecha': self.__fecha
        }
        self.transacciones.append(transaccion)

    
    def guardar_transacciones(self):
        try:
            with open("transacciones.json", 'r') as f:
                datos_previos = json.load(f)
        except FileNotFoundError:
            datos_previos = []
        
        datos_actuales = datos_previos + self.transacciones
        
        with open("transacciones.json", 'w') as f:
            json.dump(datos_actuales, f, indent=4)

    def listar_transacciones_por_cuenta(self, codigo_cuenta):
        transacciones_cuenta = []
        with open("transacciones.json", 'r') as f:
            data = json.load(f)
            for transaccion in data:
                if transaccion['codigo_cuenta'] == codigo_cuenta:
                    transacciones_cuenta.append(transaccion)
        return transacciones_cuenta



if __name__ == '__main__':
    fecha_actual = datetime.datetime.now()   
    fecha_actual_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

# # ----------probar el metodo __str__-----------------
#     historial = Historial()
#     historial.set_codigo_cuenta(12345)
#     historial.set_tipo_transaccion('Deposito')
#     historial.set_fecha(fecha_actual_formateada)
#     print(historial)

# #-------------------Pruebas de los getter y setter------------------
#     historial = Historial()
#     historial.set_codigo_cuenta(1)
#     historial.set_tipo_transaccion('Deposito')
#     historial.set_fecha('2023-05-25')

#     codigo_inicial = historial.get_codigo_cuenta()
#     tipo_inicial = historial.get_tipo_transaccion()
#     fecha_inicial = historial.get_fecha()

#     print(codigo_inicial)  
#     print(tipo_inicial)  
#     print(fecha_inicial)  
    
# # modificacion de datos
#     historial = Historial()
#     historial.set_codigo_cuenta(1)
#     historial.set_tipo_transaccion('Retiro')
#     historial.set_fecha(fecha_actual_formateada)

#     codigo_modificado = historial.get_codigo_cuenta()
#     tipo_modificado = historial.get_tipo_transaccion()
#     fecha_modificada = historial.get_fecha()

#     print(codigo_modificado)  
#     print(tipo_modificado)  
#     print(fecha_modificada)   


# # --------------------------esta parte es para probar el El guardado de instacian en JSON-------------------
    historial = Historial()

    historial.set_codigo_cuenta("8")
    historial.set_tipo_transaccion('Deposito')
    historial.set_fecha(fecha_actual_formateada)
    historial.agregar_transaccion()
    historial.guardar_transacciones()

# # --------------------------esta parte es para probar el metodo de listado por cuenta-------------------
#     historial = Historial()
#     transacciones_cuenta = historial.listar_transacciones_por_cuenta(6)
#     for transaccion in transacciones_cuenta:
#         print(transaccion)

    
    








