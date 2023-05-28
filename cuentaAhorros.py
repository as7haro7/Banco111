from datetime import datetime
from cuenta import Cuenta
class CuentaAhorros(Cuenta):
    def __init__(self, codigo_cuenta, codigo_cliente, saldo, interes_ganado):
        super().__init__(codigo_cuenta, codigo_cliente, saldo)
        self.__interes_ganado = interes_ganado

    def get_interes_ganado(self):
        return self.__interes_ganado

    def set_interes_ganado(self, interes_ganado):
        self.__interes_ganado = interes_ganado


if __name__ == '__main__':
    cuenta_ahorros = CuentaAhorros("CA001", "CL001", 1000.0, 0.05)

    codigo_cuenta = cuenta_ahorros.get_codigo_cuenta()
    codigo_cliente = cuenta_ahorros.get_codigo_cliente()
    saldo = cuenta_ahorros.get_saldo()
    interes_ganado = cuenta_ahorros.get_interes_ganado()

    print("Código de cuenta:", codigo_cuenta)
    print("Código de cliente:", codigo_cliente)
    print("Saldo:", saldo)
    print("Interés ganado:", interes_ganado)

    cuenta_ahorros.set_codigo_cuenta("CA002")
    cuenta_ahorros.set_codigo_cliente("CL002")
    cuenta_ahorros.set_saldo(1500.0)
    cuenta_ahorros.set_interes_ganado(0.08)

    nuevo_codigo_cuenta = cuenta_ahorros.get_codigo_cuenta()
    nuevo_codigo_cliente = cuenta_ahorros.get_codigo_cliente()
    nuevo_saldo = cuenta_ahorros.get_saldo()
    nuevo_interes_ganado = cuenta_ahorros.get_interes_ganado()

    print("Nuevo código de cuenta:", nuevo_codigo_cuenta)
    print("Nuevo código de cliente:", nuevo_codigo_cliente)
    print("Nuevo saldo:", nuevo_saldo)
    print("Nuevo interés ganado:", nuevo_interes_ganado)



