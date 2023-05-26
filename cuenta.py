class Cuenta:
    def _init_(self, codigo_cuenta, codigo_cliente, saldo):
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

    



# crear metodos: retiro, deposito, estracto

 

    def retiro(self, valor):
        if self.monto >= valor:
           self.monto -= valor
           self.historial.append(f"Retiro: {valor}")
        else:
            print("Error: Fondos insuficientes para realizar el retiro.")

    def deposito(self, valor):
        self.monto += valor
        self.historial.append(f"Depósito: {valor}")

    def extracto(self):
        return self.historial





if __name__ == '__main__':

    cuenta.set_codigo_cliente(1)
    cuenta.set_codigo_cuenta(1)
    cuenta.set_saldo(99)
