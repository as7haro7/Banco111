import json
class Historial:
    def __init__(self, codigo_cuenta, tipo_transaccion, fecha):
        self.transacciones = []
        self.__codigo_cuenta = codigo_cuenta
        self.__tipo_transaccion = tipo_transaccion
        self.__fecha = fecha

    def __str__(self):
        return f'codigo cuenta: {self.__codigo_cuenta}, tipo de transaccion: {self.__tipo_transaccion}, fecha: {self.__fecha}'

    # getters
    def get_codigo_cuenta(self):
        return self.__codigo_cuenta

    def get_tipo_transaccion(self):
        return self.__tipo_transaccion
    
    def get_fecha(self):
        return self.__fecha
    
    # setters    
    def set_codigo_cuenta(self, codigo_cuenta):
        self.__codigo_cuenta = codigo_cuenta

    def set_tipo_transaccion(self, tipo_transaccion):
        self.__tipo_transaccion = tipo_transaccion

    def set_fecha(self, fecha):
        self.__fecha = fecha



# metodos         
    # @staticmethod
    # def ListarHistorial(diccionario_historial, codigo):
    #     for codigo, historial in diccionario_historial.items():
    #         if codigo == codigo_cuenta:
    #             return(historial)
            

    
    def agregar_transaccion(self, codigo_cuenta, tipo_transaccion, fecha):
        transaccion = {
            'tipo_transaccion': tipo_transaccion,
            'fecha': fecha
        }
        if codigo_cuenta in self.transacciones:
            self.transacciones[codigo_cuenta].append(transaccion)
        else:
            self.transacciones[codigo_cuenta] = [transaccion]

    def guardar_transacciones(self, archivo):
        with open(archivo, 'w') as file:
            json.dump(self.transacciones, file)

if __name__ == '__main__':
    historial = Historial()
    historial.agregar_transaccion(123, 'Depósito', '2023-05-25')
    historial.agregar_transaccion(123, 'Retiro', '2023-05-26')
    historial.guardar_transacciones('transacciones.json')





# historial = Historial(codigo_cuenta=1, tipo_transaccion="Depósito", fecha="01/01/2023")
# print(historial)

# # Usar los métodos getter para obtener los valores de los atributos
# codigo_cuenta = historial.get_codigo_cuenta()
# tipo_transaccion = historial.get_tipo_transaccion()
# fecha = historial.get_fecha()
# print(codigo_cuenta, tipo_transaccion, fecha)

# # Usar los métodos setter para actualizar los valores de los atributos
# historial.set_codigo_cuenta(2)
# historial.set_tipo_transaccion("Retiro")
# historial.set_fecha("02/01/2023")
# print(historial.get_codigo_cuenta(), historial.get_tipo_transaccion(), historial.get_fecha())




# # Prueba de que estan funcionando los metodos
# historial = {} 

# historial1 = Historial(codigo_cuenta=1, tipo_transaccion="Deposito", fecha="01/01/2023")
# historial[historial1._codigo_cuenta] = historial1

# historial2 = Historial(codigo_cuenta=2, tipo_transaccion="Retiro", fecha="02/01/2023")
# historial[historial2._codigo_cuenta] = historial2

# historial3 = Historial(codigo_cuenta=3, tipo_transaccion="Transferencia", fecha="03/01/2023")
# historial[historial3._codigo_cuenta] = historial3


# # Guardar el diccionario en un archivo JSON con la función de serialización personalizada
# with open("historial.json", "w") as archivo_json:
#     json.dump(historial, archivo_json, default=Historial.serializar_historial)


# codigo_prueba = 1
# cuenta_x=Historial.ListarHistorial(historial,codigo_prueba)
# print(cuenta_x)