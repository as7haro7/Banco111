# pip install simple-term-menu
#!/usr/bin/env python3

import json
import datetime

# import os
# from simple_term_menu import TerminalMenu

from historial import Historial
import personas
def imprimirMenu(lista):
    for i in lista:
        print(i)


def main(): 
    fecha_actual = datetime.datetime.now()   
    fecha_actual_formateada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

    op=0  
    opciones = ["[1] Personas","[2] op2","[3] op3","[4] Historial","[5] Configuracion","[8] salir"]
 
    

    terminar=False
    while True:
        op=0  
        imprimirMenu(opciones)
        op=input("\nIngrese una opcion - Menu Principal: ") 
        if int(op)==1:
		
            opS1=0
            USU = personas.persona('none', 'none', 'none', 'none', 'none', 'none')
            submenu=["[1] Agregar Persona nueva","[2] Pedir datos de una persona","[3] cambiar datos de una persona",'[4] enlistar personas','[5] Salir']

            while True:
                imprimirMenu(submenu)
                opS1 = input("\nIngrese una opcion : ")
                if int(opS1)==1:
                    print("--------------AGREGANDO PERSONA NUEVA--------------")
                    USU.nueva_persona()
                    print("-----------------------------------")
                    print("----------AGREGADO CON EXITO-------")
                    print("-----------------------------------")
                elif int(opS1)==2:

                    usuario=USU.obtener_persona(input(f'INGRESE APELLIDOS :\n'),input(f'INGRESE NOMBRES :\n'))
                    if usuario==False:  print(f'EL USUARIO INGRESADO NO EXISTE')
                    else:
                        submenu=["[1] CODIGO DE CLIENTE","[2] NOMBRES",'[3] APELLIDOS','[4] CEDULA DE IDENTIDAD','[5] DIRECCION','[6] REFERENCIA',"[7] salir"]

                        while True:
                            imprimirMenu(submenu)
                            opS1 = int(input("Ingrese el numero de dato que desea saber: "))
                            if opS1==1:print('\nEL DATO SOLICITADO ES------>',usuario.get_codigo_cliente(),'\n')
                            elif opS1==2:print('\nEL DATO SOLICITADO ES------>',usuario.get_nombres(),'\n')
                            elif opS1==3:print('\nEL DATO SOLICITADO ES------>',usuario.get_apellidos(),'\n')
                            elif opS1==4:print('\nEL DATO SOLICITADO ES------>',usuario.get_cedula_identidad(),'\n')
                            elif opS1==5:print('\nEL DATO SOLICITADO ES------>',usuario.get_direccion(),'\n')
                            elif opS1==6:print('\nEL DATO SOLICITADO ES------>',usuario.get_referencia(),'\n')
                            elif opS1==7:break

                elif int(opS1)==3:
                    usuario=USU.obtener_persona(input(f'INGRESE APELLIDOS :\n'),input(f'INGRESE NOMBRES :\n'))
                    if usuario==False:  print(f'EL USUARIO INGRESADO NO EXISTE')
                    else:
                        submenu=["[1] NOMBRES",'[2] APELLIDOS','[3] CEDULA DE IDENTIDAD','[4] DIRECCION','[5] REFERENCIA',"[6] salir"]
                        while True:
                            opS1 = int(input("Ingrese el numero de dato que desea CAMBIAR: "))
                            imprimirMenu(submenu)
                            if opS1==1:
                                usuario.set_nombres(f'INGRESE NUEVOS NOMBRES')
                                print('\nEL DATO AHORA ES ES------>',usuario.get_nombres(),'\n')
                            elif opS1==2:
                                usuario.set_apellidos(f'INGRESE NUEVOS APELLIDOS')
                                print('\nEL DATO AHORA ES ES------>',usuario.get_apellidos(),'\n')
                            elif opS1==3:
                                usuario.set_cedula_identidad(f'INGRESE NUEVA CI')
                                print('\nEL DATO AHORA ES ES------>',usuario.get_cedula_identidad(),'\n')
                            elif opS1==4:
                                usuario.set_direccion(f'INGRESE NUEVA DIRECCION')
                                print('\nEL DATO AHORA ES ES------>',usuario.get_direccion(),'\n')
                            elif opS1==5:
                                usuario.set_referencia(input(f'INGRESE NUEVA REFERENCIA'))
                                print('\nEL DATO AHORA ES ES------>',usuario.get_referencia(),'\n')
                            elif opS1==6:break
                elif int(opS1)==4:print(USU.enlistar_personas())
                elif int(opS1)==5:break        
        elif int(op)==4:
            opS4=0
            submenu=["[1] Agregar a historial","[2] Listar historial de una cuenta","[3] salir"]            
            while True:
                imprimirMenu(submenu)
                opS4=input("Ingrese opcion para SubMenu: Historial ")

                if int(opS4)==1:
                    print("--------------AGREGAR--------------")                  

                    historial = Historial()                    
                    historial.set_codigo_cuenta(int(input("Codigo Cuenta: ")))
                    historial.set_tipo_transaccion(input("Tipo de transaccion?> "))
                    historial.set_fecha(fecha_actual_formateada)
                    historial.agregar_transaccion()
                    historial.guardar_transacciones()
                    print("-----------------------------------")
                    print("----------AGREGADO CON EXITO-------")
                    print("-----------------------------------")

                if int(opS4)==2:
                    print("--------------LISTAR--------------")
                    historial = Historial()
                    transacciones_cuenta = historial.listar_transacciones_por_cuenta(int(input("Codigo Cuenta: ")))
                    for transaccion in transacciones_cuenta:
                        print(transaccion)
                    print("-----------------------------------")
    

                if int(opS4)==3:
                    break
            # op=0

        elif int(op)==5:
            conf=[]
            with open('configuracion.cfg.json', 'r') as f:
                datos = json.load(f)                

            print(datos)

            

           
        elif int(op)==8:
            break     

        
        print(op)




if __name__ == "__main__":
    main()