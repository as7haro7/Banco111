import os
import sys
import time
import json
import datetime

from historial import Historial

def imprimir_diccionario(diccionario):
    print("*" * 40)
    for clave, valor in diccionario.items():
        print(f"* \033[1m{clave}:\033[0m {valor}")
    print("*" * 40)

def estilo_banco_patito():
    print("\033[1;36m")  # Establece el color del texto a cian brillante y negrita                                   

    # print("888b.                          888b.       w   w  w         ")
    # print("8wwwP .d88 8d8b. .d8b .d8b.    8  .8 .d88 w8ww w w8ww .d8b. ")
    # print("8   b 8  8 8P Y8 8    8' .8    8wwP' 8  8  8   8  8   8' .8 ")
    # print("888P' `Y88 8   8 `Y8P `Y8P'    8     `Y88  Y8P 8  Y8P `Y8P' ")  

    print("(|~  |~) _  _  _ _   |~) _ _|_|_ _   (|~") 
    print("_|)  |_)(_|| |(_(_)  |~ (_| ||| (_)  _|)")                                         
                                      

    print("\033[0m")  # Restablece los estilos por defecto




def mostrar_menu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    estilo_banco_patito()
    # print("===========================================")
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
    # print("===========================================")
    


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
    


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida): 
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones_principal = {
        '1': ('Gestión de Personas', submenu_gestion_personas),
        '2': ('Gestión de Cuentas', submenu_gestion_cuentas),
        '3': ('Ver Configuración del Banco', submenu_configuracion_banco),
        '4': ('Salir', salir)
    }

    generar_menu('Menu Principal', opciones_principal, '4')

def submenu_gestion_personas():
    opciones_personas = {
        '1': ('Agregar Persona nueva', agregarPersona),
        '2': ('Pedir datos de una persona', pedirDatosPersona),
        '3': ('Cambiar datos de una persona', cambiarDatosPersona),
        '4': ('Enlistar personas', enlistarPersonas),
        '5': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Personas', opciones_personas, '5')

def submenu_gestion_cuentas():
    opciones_cuentas = {
        '1': ('Crear una cuenta', crearCuenta),
        '2': ('Realizar un depósito', realizarDeposito),
        '3': ('Realizar un retiro', realizarRetiro),
        '4': ('Calcular interés', calcularInteres),
        '5': ('Mostrar extracto', mostrarExtracto),
        '6': ('Listar historial', listarHistorial),
        '7': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Cuentas', opciones_cuentas, '7')

def submenu_configuracion_banco():
    opciones_configuracion = {
        '1': ('Ver datos del Banco', verDatosBanco),       
        '2': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Configuración del Banco', opciones_configuracion, '2')

def agregarPersona():
    # Lógica para agregar una nueva persona
    pass

def pedirDatosPersona():
    # Lógica para pedir datos de una persona
    pass

def cambiarDatosPersona():
    # Lógica para cambiar datos de una persona
    pass

def enlistarPersonas():
    # Lógica para enlistar personas
    pass

def crearCuenta():
    # Lógica para crear una cuenta
    pass

def realizarDeposito():
    # Lógica para realizar un depósito
    pass

def realizarRetiro():
    # Lógica para realizar un retiro
    pass

def calcularInteres():
    # Lógica para calcular el interés
    pass

def mostrarExtracto():
    # Lógica para mostrar el extracto
    pass

def listarHistorial():
    historial = Historial()
    transacciones_cuenta = historial.listar_transacciones_por_cuenta(input("Codigo Cuenta: "))
    for transaccion in transacciones_cuenta:
        print(transaccion)
    pass

def verDatosBanco():
    with open('configuracion.cfg.json', 'r') as f:
        datos = json.load(f)    
    imprimir_diccionario(datos)

def salir_sub_menu():
    animacion_carga(1/2,"Saliendo")

def animacion_carga(duracion,mensaje):
    animacion = '|/-\\'
    idx = 0
    
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < duracion:
        sys.stdout.write('\r' + mensaje+" " + animacion[idx])
        sys.stdout.flush()
        idx = (idx + 1) % len(animacion)
        time.sleep(0.1)

def salir():
    print('\nSaliendo...')
    # print('Cerrando sesión...')
    msg=('Guardando cambios')

    animacion_carga(4,msg)
    os.system('clear') 
    print('\n¡Gracias por elegir Banco Patito! ¡Hasta pronto! 🦆💰')

if __name__ == '__main__':
    os.system('clear')    
    menu_principal() # iniciamos el programa mostrando el menú principal