from datetime import datetime
from cuenta import Cuenta
class CuentaAhorros(Cuenta):
    # def __init__(self, codigo_cuenta, saldo_inicial=0):
    #     super().__init__(codigo_cuenta, saldo_inicial)
    #     self.interes_ganado = 0
    def __init__(self, codigo_cuenta, codigo_cliente, saldo=0, tasa_interes=0 ):
        super().__init__(codigo_cuenta, codigo_cliente, saldo)
        self.tasa_interes  = __tasa_interes 

    def agregar_intereses(self, tasa_interes, fecha_fin_periodo):
        fecha_inicio_periodo = datetime.strptime(self.transacciones[-1][0], "%Y-%m-%d %H:%M:%S").date()
        dias = (fecha_fin_periodo - fecha_inicio_periodo).days
        intereses = self.saldo * __tasa_interes / 100 / 365 * dias
        self.interes_ganado += intereses
        self.saldo += intereses

    def calculo_interes(self):
        interes = self.monto * self.__tasa_interes
        self.monto += interes
        self.historial.append(f"Interés calculado: {interes}")


if __name__ == '__main__':
    # Crear una cuenta de ahorros
    cuenta_ahorros = CuentaAhorros(2000, 0.05)

    # Realizar operaciones en la cuenta de ahorros
    cuenta_ahorros.deposito(1000)
    cuenta_ahorros.retiro(500)
    cuenta_ahorros.calculo_interes()
