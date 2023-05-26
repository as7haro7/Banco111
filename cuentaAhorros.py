from cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, codigo_cuenta, codigo_cliente, saldo, interes_ganado):
        super().__init__(codigo_cuenta, codigo_cliente, saldo)
        self.interes_ganado = interes_ganado

