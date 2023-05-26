import json
class Historial:
    def __init__(self, codigo_cuenta, tipo_transaccion, fecha):
        self._codigo_cuenta = codigo_cuenta  #dato privado
        self._tipo_transaccion = tipo_transaccion  #dato privado
        self._fecha = fecha  #dato privado

    def __str__(self):
        return f'codigo cuenta: {self._codigo_cuenta}, tipo de transaccion: {self._tipo_transaccion}, fecha: {self._fecha}'



# getters y setters creo ggg
    def get_codigo_cuenta(self):
        return self._codigo_cuenta #privado

    def set_codigo_cuenta(self, codigo_cuenta):
        self._codigo_cuenta = codigo_cuenta #privado

    def get_tipo_transaccion(self):
        return self._tipo_transaccion #privado

    def set_tipo_transaccion(self, tipo_transaccion):
        self._tipo_transaccion = tipo_transaccion #privado

    def get_fecha(self):
        return self._fecha #privado

    def set_fecha(self, fecha):
        self._fecha = fecha #privado



# metodos         
    @staticmethod
    def ListarHistorial(diccionario_historial, codigo):
        for codigo, historial in diccionario_historial.items():
            if codigo == codigo_cuenta:
                return(historial)
            

    def serializar_historial(obj):
        if isinstance(obj, Historial):
            return {
                "codigo_cuenta": obj._codigo_cuenta,
                "tipo_transaccion": obj._tipo_transaccion,
                "fecha": obj._fecha
            }
        raise TypeError(f"El objeto {obj.__class__.__name__} no es serializable.")

    
    def guardar_en_historial(historial):
        # Leer el contenido existente del archivo JSON
        try:
            with open("historial.json", "r") as archivo_json:
                historial_existente = json.load(archivo_json)
        except FileNotFoundError:
            historial_existente = {}

        # Obtener el código de cuenta del historial
        codigo_cuenta = historial["_codigo_cuenta"]

        # Verificar si el código de cuenta ya existe en el historial existente
        if codigo_cuenta in historial_existente:
            # Si existe, agregar el nuevo historial a la lista existente
            historial_existente[codigo_cuenta].append(historial)
        else:
            # Si no existe, crear una nueva lista con el historial y asignarla al código de cuenta
            historial_existente[codigo_cuenta] = [historial]

        # Guardar el historial actualizado en el archivo JSON
        with open("historial.json", "w") as archivo_json:
            json.dump(historial_existente, archivo_json)








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