# pip install simple-term-menu
#!/usr/bin/env python3

import os
from simple_term_menu import TerminalMenu

from historial import Historial

def main():   
    opciones = ["[1] op1","[2] op2","[3] op3","[4] Historial","[5] op5","[6] op6","[7] op7","[8] salir"]
    menuPrincipal=TerminalMenu(opciones,title="Menu Principal")
    subMenu = TerminalMenu(["opcion 1", "opcion 2"],title="subMenu")

    

    terminar=False
    while terminar == False:
        índiceDeOpción = menuPrincipal.show()
        opcionElegida=opciones[índiceDeOpción]

        if opcionElegida=="[2] op2":
            subMenu.show()

        if opcionElegida=="[4] Historial":
            # historial1 = {"codigo_cuenta": 1, "tipo_transaccion": "Depósito", "fecha": "01/01/2023"}            
            # print(historial1)
            historial1 = {
                "codigo_cuenta": 1,
                "tipo_transaccion": "Deposito",
                "fecha": "01/01/2023"
            }
            Historial.guardar_en_historial(historial1)


        if opcionElegida=="[8] salir":
            terminar=True
        else: 
            print(opcionElegida)



if __name__ == "__main__":
    main()