import os
import platform
import sys
import time
import json
import datetime

import personas
from cuenta import Cuenta
from historial import Historial
import cuenta_ahorros
def imprimir_diccionario(diccionario):
    print("*" * 40)
    for clave, valor in diccionario.items():
        print(f"* \033[1m{clave}:\033[0m {valor}")
    print("*" * 40)

def estilo_banco_patito():
    print("\033[1;36m")  # Establece el color del texto a cian brillante y negrita                                   
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
        '2': ('Pedir datos de una persona', submenu_pedirDatosPersona_post),
        '3': ('Cambiar datos de una persona', submenu_cambiarDatosPersona_post),
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
    
# -----------------------------------------------------------------------------------------------------

def agregarPersona():
    personas.persona.nueva_persona()


def submenu_pedirDatosPersona_post():
    print(f'COMO DESEA OBTENER SUS DATOS??')
    opciones_personas = {
        '1': ('INGRESANDO NOMBRES Y APELLIDOS', MedioNombresApellidos),
        '2': ('INGRESANDO CODIGO DE USUARIO', MedioCodigoUsuario),
        '3': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Cuentas', opciones_personas, '3')

def MedioNombresApellidos():
    global gg
    nombres=input(f'INGRESE SUS NOMBRES------------>')
    apellidos=input(f'INGRESE SUS APELLIDOS------------>')
    gg=personas.persona.obtener_persona(apellidos,nombres)
    if gg==False:print(f'El usuario ingresado no existe')
    else:submenu_pedirDatosPersona()

def MedioCodigoUsuario():
    global gg
    codigo=input(f'INGRESE SU CODIGO DE USUARIO------------------>')
    gg=personas.persona.obtener_persona_codigo_usuario(codigo)
    if gg==False:print(f'El usuario ingresado no existe')
    else:submenu_pedirDatosPersona()


def submenu_pedirDatosPersona():
    print(f'Elija el dato que quiera saber')
    opciones_personas = {
        '1': ('Pedir Codigo de Usuario', PedirCodigoUsuario),
        '2': ('Pedir Nombres', PedirNombres),
        '3': ('Pedir Apellidos', PedirApellidos),
        '4': ('Pedir Carnet de Identaidad', PedirCarnetIdentidad),
        '5': ('Pedir Direccion', PedirDireccion),
        '6': ('Pedir Referencia', PedirReferencia),
        '7': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Cuentas', opciones_personas, '7')

def PedirCodigoUsuario():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_codigo_cliente()}')
def PedirNombres():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_nombres()}')
def PedirApellidos():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_apellidos()}')
def PedirCarnetIdentidad():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_cedula_identidad()}')
def PedirDireccion():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_direccion()}')
def PedirReferencia():
    global gg
    print(f'EL DATO PEDIDO ES ---------->{gg.get_referencia()}')

def submenu_cambiarDatosPersona_post():
    global gg2
    codigo=input(f'INGRESE SU CODIGO DE USUARIO------------------>')
    gg2=personas.persona.obtener_persona_codigo_usuario(codigo)
    if gg2==False:print(f'El usuario ingresado no existe')
    else:cambiarDatosPersona()

def cambiarDatosPersona():
    print(f'Elija el dato que decea cambiar')
    opciones_personas = {
        '1': ('Cambiar Nombres', ChangeNombres),
        '2': ('Cambiar Apellidos', ChangeApellidos),
        '3': ('Cambiar Carnet de Identaidad', ChangeCarnetIdentidad),
        '4': ('Cambiar Direccion', ChangeDireccion),
        '5': ('Cambiar Referencia', ChangeReferencia),
        '6': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Cuentas', opciones_personas, '6')

def ChangeNombres():
    global gg2
    nuevo=input(f'INGRESE NUEVO DATO----------------->')
    gg2.set_nombres(nuevo,True)
    
def ChangeApellidos():
    global gg2
    nuevo=input(f'INGRESE NUEVO DATO----------------->')
    gg2.set_apellidos(nuevo,True)
    
def ChangeCarnetIdentidad():
    global gg2
    nuevo=input(f'INGRESE NUEVO DATO----------------->')
    gg2.set_cedula_identidad(nuevo,True)
    
def ChangeDireccion():
    global gg2
    nuevo=input(f'INGRESE NUEVO DATO----------------->')
    gg2.set_direccion(nuevo,True)
    
def ChangeReferencia():
    global gg2
    nuevo=input(f'INGRESE NUEVO DATO----------------->')
    gg2.set_referencia(nuevo,True)
    

def enlistarPersonas():
    print(f'ESTA ES LA LISTA DE TODAS LAS PERSONAS\n{personas.persona.enlistar_personas()}\n')
# -----------------------------------------------------------------------------------------------------

def crearCuenta():
    cod_cliente=input("Codigo de Cliente: ")
    cuenta = Cuenta(None,cod_cliente,0)

    if personas.persona.ob_per_code(cod_cliente)==True:
        cargar_anim()
        print("*" * 40)
        cuenta.guardar_cuenta()
        print("*" * 40)
    else:
        cargar_anim()
        print("*" * 40)
        print("Error, Primero Registre Persona")
        print("*" * 40)


def guardarHistorial(cuenta,tipo_transacion):
    fecha_actual = datetime.datetime.now()   
    fecha_actual_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')
    historial = Historial()
    historial.set_codigo_cuenta(cuenta)
    historial.set_tipo_transaccion(tipo_transacion)
    historial.set_fecha(fecha_actual_formateada)
    historial.agregar_transaccion()
    # cargar_anim()
    historial.guardar_transacciones() 

def realizarDeposito():
    cod_cuenta=input("Codigo de cuenta: ")
    cuenta = Cuenta(cod_cuenta, None,None)
    print("*" * 40)
    monto=int(input("Monto a depositar: "))
    dep=cuenta.deposito(monto)
    cargar_anim()
    if dep==True:
        guardarHistorial(cod_cuenta,"Deposito")
        print("Deposito con exito")
    else:
        print("Cuenta no encontrada")
    print("*" * 40)

def realizarRetiro():
    cod_cuenta=input("Codigo de cuenta: ")
    cuenta = Cuenta(cod_cuenta, None,None)
    print("*" * 40)
    monto=int(input("Monto a depositar: "))
    ret=cuenta.retiro(monto)
    cargar_anim()
    if ret=="Retiro realizado exitosamente":
        guardarHistorial(cod_cuenta,"Retiro")
        print(ret)
    else:
        print(ret)
    print("*" * 40)
# ----------------------------------------------------------------

def calcularInteres():
    opciones_personas = {
        '1': ('Verificar intereses', VerificarInteres),
        '2': ('siguiente dia', SiguienteDia),
        '3': ('Salir', salir_sub_menu)
    }

    generar_menu('Submenú Gestión de Cuentas', opciones_personas, '3')

def VerificarInteres():
    CUENTA=input(f'INTRODUCE TU NUMERO DE CUENTA')
    cuentita=Cuenta(CUENTA,'none','none')
    cuentita.obtener_datos_cuenta()
    cuenta_ahorros.CuentaAhorros.mostrar_intereses(cuentita)

def SiguienteDia():
    cuenta_ahorros.CuentaAhorros.calculo_de_interes()
    
# ----------------------------------------------------------------
def mostrarExtracto():
    cuenta = Cuenta(input("Codigo de Cuenta: "), None,None)  
    datos_cuenta = cuenta.obtener_datos_cuenta()
    cargar_anim()
    imprimir_diccionario(datos_cuenta)
    

def listarHistorial():
    historial = Historial()
    transacciones_cuenta = historial.listar_transacciones_por_cuenta(input("Codigo de cuenta: "))
    cargar_anim()
    for transaccion in transacciones_cuenta:
        imprimir_diccionario(transaccion)     

def verDatosBanco():
    with open('configuracion.cfg.json', 'r') as f:
        datos = json.load(f) 
    cargar_anim()   
    imprimir_diccionario(datos)

def salir_sub_menu():
    animacion_carga(1/2,"Saliendo")

def cargar_anim():
    animacion_carga(1,"Cargando")
    print("\n")


def animacion_carga(duracion,mensaje):
    animacion = '|/-\\'
    idx = 0
    
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < duracion:
        sys.stdout.write('\r' + mensaje+" " + animacion[idx])
        sys.stdout.flush()
        idx = (idx + 1) % len(animacion)
        time.sleep(0.1)

def limpiar_consola():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def salir():
    print('\nSaliendo...')
    msg=('Guardando cambios')

    animacion_carga(4,msg)
    limpiar_consola() 
    print('\n¡Gracias por elegir Banco Patito! ¡Hasta pronto! 🦆💰')



if __name__ == '__main__':
    limpiar_consola()    
    menu_principal() 