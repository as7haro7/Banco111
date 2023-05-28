import json
import random


class Cuenta:
    def __init__(self, codigo_cuenta, codigo_cliente, saldo):
        self.__codigo_cuenta = codigo_cuenta
        self.__codigo_cliente = codigo_cliente
        self.__saldo = saldo

    def get_codigo_cuenta(self):
        return self.__codigo_cuenta

    def get_codigo_cliente(self):
        return self.__codigo_cliente

    def get_saldo(self):
        return self.__saldo

    def set_codigo_cuenta(self, codigo_cuenta):
        self.__codigo_cuenta = codigo_cuenta

    def set_codigo_cliente(self, codigo_cliente):
        self.__codigo_cliente = codigo_cliente

    def set_saldo(self, saldo):
        self.__saldo = saldo

    

    # METODOS DE CLASE
    def generar_codigo_cliente(self):        
        prefijo = "CL"
        sufijo = str(random.randint(1000, 99999))   
        return prefijo + sufijo
    
    def guardar_cuenta(self):
        self.__codigo_cliente = self.generar_codigo_cliente()

        cuenta_data = {
            "codigo_cuenta": self.__codigo_cuenta,
            "codigo_cliente": self.__codigo_cliente,
            "saldo": self.__saldo
        }

        cuentas = []

        # Verificar si ya existe una cuenta con el mismo código de cuenta
        try:
            with open("cuenta.json", "r") as file:
                cuentas = json.load(file)

                for cuenta in cuentas:
                    if cuenta["codigo_cuenta"] == self.__codigo_cuenta:
                        print(f"Error: Ya existe una cuenta con el código {self.__codigo_cuenta}")
                        return
        except FileNotFoundError:
            pass

        cuentas.append(cuenta_data)

        with open("cuenta.json", "w") as file:
            json.dump(cuentas, file,indent=4)
            print("Cuenta guardada exitosamente en cuenta.json")

    def deposito(self, monto):
        try:
            with open("cuenta.json", "r") as file:
                cuentas = json.load(file)
        except FileNotFoundError:
            cuentas = []

        for cuenta in cuentas:
            if cuenta["codigo_cuenta"] == self.__codigo_cuenta:
                cuenta["saldo"] += monto
                break 
        else:
            # Si no se encontró la cuenta, agregar una nueva cuenta a la lista
            # cuentas.append({
            #     "codigo_cuenta": self.__codigo_cuenta,
            #     "codigo_cliente": self.__codigo_cliente,
            #     "saldo": self.__saldo + monto
            # })
            print("Cuenta no encontrada")
            return

        with open("cuenta.json", "w") as file:
            json.dump(cuentas, file,indent=4)
            print("Depósito realizado exitosamente")

    def retiro(self, monto):
        try:
            with open("cuenta.json", "r") as file:
                cuentas = json.load(file)
        except FileNotFoundError:
            cuentas = []

        for cuenta in cuentas:
            if cuenta["codigo_cuenta"] == self.__codigo_cuenta:
                if cuenta["saldo"] >= monto:
                    cuenta["saldo"] -= monto
                    break 
                else:
                    print("Saldo insuficiente para realizar el retiro")
                    return
        else:
            print("Cuenta no encontrada")
            return

        with open("cuenta.json", "w") as file:
            json.dump(cuentas, file,indent=4)
            print("Retiro realizado exitosamente")

    # EN PROCESO...

    def extracto(self):
        extracto = {
            'codigo_cuenta': self.__codigo_cuenta,
            'codigo_cliente': self.__codigo_cliente,
            'saldo': self.__saldo,
            'transacciones': []
        }

        with open('transacciones.json') as file:
            transacciones = json.load(file)

            cuenta_encontrada = False
            for transaccion in transacciones:
                if transaccion['codigo_cuenta'] == self.__codigo_cuenta:
                    cuenta_encontrada = True
                    extracto['transacciones'].append(transaccion)

            if not cuenta_encontrada:
                return 'La cuenta no existe en el historial de transacciones.'
        return extracto



    def obtener_datos_cuenta(self):
        with open('cuenta.json') as file:
            cuentas = json.load(file)

        for cuenta in cuentas:
            if cuenta['codigo_cuenta'] == self.__codigo_cuenta:
                return {
                    'codigo_cuenta': cuenta['codigo_cuenta'],
                    'codigo_cliente': cuenta['codigo_cliente'],
                    'saldo': cuenta['saldo']
                }
        return None



if __name__ == '__main__':
    # print("cuenta")

    # # PRUEBA DE METODOS GETER Y SETER

    # cuenta = Cuenta("C001", "CL001", 1000.0)
    # codigo_cuenta = cuenta.get_codigo_cuenta()
    # codigo_cliente = cuenta.get_codigo_cliente()
    # saldo = cuenta.get_saldo()

    # print("Código de cuenta:", codigo_cuenta)
    # print("Código de cliente:", codigo_cliente)
    # print("Saldo:", saldo)


    # # modificar
    # cuenta.set_codigo_cuenta("C002")
    # cuenta.set_codigo_cliente("CL002")
    # cuenta.set_saldo(1500.0)

    # nuevo_codigo_cuenta = cuenta.get_codigo_cuenta()
    # nuevo_codigo_cliente = cuenta.get_codigo_cliente()
    # nuevo_saldo = cuenta.get_saldo()

    # print("Nuevo código de cuenta:", nuevo_codigo_cuenta)
    # print("Nuevo código de cliente:", nuevo_codigo_cliente)
    # print("Nuevo saldo:", nuevo_saldo)



    # PRUEBA DE METODO DE GUARDAR CUENTA
    cuenta = Cuenta("98", None,0)
    cuenta.guardar_cuenta()

    # # PRUEBA DE DEPOSITO DE CUENTA
    # cuenta = Cuenta("1", None,None)
    # cuenta.deposito(50)
    
    # # PRUEBA DE RETIRO DE CUENTA
    # cuenta = Cuenta("1", None,None)
    # cuenta.retiro(50)



    
    # # ESTO ES PARA PROBAR EL ESTRACTO
    # cuenta = Cuenta("1", None,None)  
    # datos_cuenta = cuenta.obtener_datos_cuenta()
    # print(datos_cuenta,type(datos_cuenta))
    # # c=Cuenta.obtener_datos_cuenta()
    # # print(c)
    # # cuenta = Cuenta("198", None,None)
    # # ext=cuenta.extracto()
    # # print(ext)