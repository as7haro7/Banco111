def mostrar_menu():
    print("===== MENÚ =====")
    print("1. Crear una cuenta")
    print("2. Realizar un depósito")
    print("3. Realizar un retiro")
    print("4. Calcular interés (solo para cuentas de ahorro)")
    print("5. Mostrar extrato")
    print("6. Listar historial")
    print("0. Salir")
    print("================")
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion


def crear_cuenta():
    # Pedir los datos necesarios para crear una cuenta
    codigo_cuenta = input("Ingrese el código de la cuenta: ")
    codigo_cliente = input("Ingrese el código del cliente: ")
    saldo = float(input("Ingrese el saldo inicial: "))

    # Crear una instancia de la clase Cuenta o CuentaAhorros según corresponda
    tipo_cuenta = input("Ingrese el tipo de cuenta (1. Cuenta / 2. Cuenta de Ahorros): ")
    if tipo_cuenta == "1":
        cuenta = Cuenta(codigo_cuenta, codigo_cliente, saldo)
    elif tipo_cuenta == "2":
        interes = float(input("Ingrese la tasa de interés: "))
        cuenta = CuentaAhorros(codigo_cuenta, codigo_cliente, saldo, interes)
    else:
        print("Opción inválida")

    return cuenta


def realizar_deposito(cuenta):
    monto = float(input("Ingrese el monto a depositar: "))
    cuenta.deposito(monto)
    print("Depósito realizado con éxito.")


def realizar_retiro(cuenta):
    monto = float(input("Ingrese el monto a retirar: "))
    cuenta.retiro(monto)
    print("Retiro realizado con éxito.")


def calcular_interes(cuenta):
    if isinstance(cuenta, CuentaAhorros):
        cuenta.calculo_interes()
        print("Cálculo de interés realizado.")
    else:
        print("Esta opción solo es válida para cuentas de ahorro.")


def mostrar_extrato(cuenta):
    cuenta.extrato()


def listar_historial(historial):
    historial.listar_historial()


if __name__ == '__main__':
    historial = Historial()
    cuenta = None

    while True:
        opcion = mostrar_menu()

        if opcion == "0":
            break
        elif opcion == "1":
            cuenta = crear_cuenta()
        elif opcion == "2":
            if cuenta:
                realizar_deposito(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == "3":
            if cuenta:
                realizar_retiro(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == "4":
            if cuenta:
                calcular_interes(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == "5":
            if cuenta:
                mostrar_extrato(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        elif opcion == "6":
            listar_historial(historial)
        else:
            print("Opción inválida")
