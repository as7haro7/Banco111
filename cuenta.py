import json
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
    def guardar_cuenta(self):
        cuenta_data = {
            "codigo_cuenta": self.__codigo_cuenta,
            "codigo_cliente": self.__codigo_cliente,
            "saldo": self.__saldo
        }

        try:
            with open("cuenta.json", "r") as file:
                cuentas = json.load(file)
        except FileNotFoundError:
            cuentas = []

        cuentas.append(cuenta_data)

        with open("cuenta.json", "w") as file:
            json.dump(cuentas, file)
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
            json.dump(cuentas, file)
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
        pass
    
    
    
    # def extracto1(self):
    #     return self.historial
        return self.historial


    def obtener_codigo_cliente(CODIGO_DE_CLIENTE):
        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.loads(f.read())
            
        for i in diccionario:
            for j in i:
                if CODIGO_DE_CLIENTE == j: return True
        return False



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



    # # PRUEBA DE METODO DE GUARDAR CUENTA
    # cuenta = Cuenta("1", "asdas",0)
    # cuenta.guardar_cuenta()

    # PRUEBA DE DEPOSITO DE CUENTA
    cuenta = Cuenta("1", None,None)
    cuenta.deposito(50)
    
    # # PRUEBA DE RETIRO DE CUENTA
    # cuenta = Cuenta("1", None,None)
    # cuenta.retiro(50)



    
    # # ESTO ES PARA PROBAR EL ESTRACTO
    # extracto = cuenta.extracto()
    # print(extracto)