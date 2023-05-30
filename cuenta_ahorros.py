from cuenta import Cuenta
import json
import datetime
import time

class CuentaAhorros(Cuenta):

    def __init__(self, codigo_cuenta, codigo_cliente, saldo, interes_ganado):
        super().__init__(codigo_cuenta, codigo_cliente, saldo)
        
        self.__interes_ganado = interes_ganado
    
    def get_interes_ganado(self):
        return self.__interes_ganado
    
    def set_interes_ganado(self, new):
        self.__interes_ganado = new


    def mostrar_intereses(self):
        with open('intereses_deposito.json', 'r') as deposito:                          #fecha actual para hacer la prueba
            all_depositos=json.loads(deposito.read())
        with open('intereses_retiro.json', 'r') as retiro:
            all_retiros=json.loads(retiro.read())
        print(f'INTERES GANADOS')
        for i in all_depositos:
            if i["_Cuenta__codigo_cuenta"]==self.get_codigo_cuenta():
                k=i["_CuentaAhorros__interes_ganado"]
                print(f'---------------{k}--------------------')
        print(f'INTERES QUE LE SON REMOVIDOS')
        for i in all_retiros:
            if i["_Cuenta__codigo_cuenta"]==self.get_codigo_cuenta():
                k=i["_CuentaAhorros__interes_ganado"]
                print(f'---------------{k}--------------------')

    def creando_cuenta_ahorro(self,monto):
        diccionario=Cuenta.obtener_datos_cuenta(self)
        return CuentaAhorros(diccionario["codigo_cuenta"],diccionario["codigo_cliente"],monto,0)
    
    def calculo_de_interes():

        CuentaAhorros.calculo_de_interes_deposito('none','none','actualizar')
        CuentaAhorros.calculo_de_interes_retiro('none','none','actualizar')

        actual=datetime.datetime.today().strftime('%d/%m/%Y')

        with open('configuracion.cfg.json', 'r') as configuracion:
            fecha=json.loads(configuracion.read())
            if f'{actual}'==fecha["finPeriodo"]:                                                #'29/05/2023'
                with open('intereses_deposito.json', 'r') as deposito:                          #fecha actual para hacer la prueba
                    all_depositos=json.loads(deposito.read())
                with open('intereses_retiro.json', 'r') as retiro:
                    all_retiros=json.loads(retiro.read())
                with open('cuenta.json', 'r') as cuentas:
                    all_cuentas=json.loads(cuentas.read())

                for search in all_cuentas:
                    for search_deposito in all_depositos:
                        if search_deposito["_Cuenta__codigo_cuenta"]==search["codigo_cuenta"] and search_deposito["_Cuenta__codigo_cliente"]==search["codigo_cliente"]:
                            search["saldo"] += round(search_deposito["_CuentaAhorros__interes_ganado"])
                            search_deposito["_CuentaAhorros__interes_ganado"]=0

                    for search_retiros in all_retiros:
                        if search_retiros["_Cuenta__codigo_cuenta"]==search["codigo_cuenta"] and search_retiros["_Cuenta__codigo_cliente"]==search["codigo_cliente"]:
                            search["saldo"] -= round(search_deposito["_CuentaAhorros__interes_ganado"])
                            search_retiros["_CuentaAhorros__interes_ganado"]=0

                with open('intereses_deposito.json', 'w') as deposito:
                    deposito.write(json.dumps(all_depositos, indent= 4))
                with open('intereses_retiro.json', 'w') as retiro:
                    retiro.write(json.dumps(all_retiros, indent= 4))
                with open('cuenta.json', 'w') as cuentas:
                    cuentas.write(json.dumps(all_cuentas, indent= 4))


    def calculo_de_interes_deposito(self,monto,instruccion='none'):
        if instruccion=='actualizar':
            with open('intereses_deposito.json', 'r') as f:
                diccionario=json.loads(f.read())
            with open('configuracion.cfg.json', 'r') as f:
                porcentaje=json.loads(f.read())
            taza_interes=porcentaje["tasaInteres"]
            for i in diccionario:
                i["_CuentaAhorros__interes_ganado"]+=i["_Cuenta__saldo"]*(taza_interes/100)*(1/360)
            with open('intereses_deposito.json','w') as f:
                f.write(json.dumps(diccionario, indent= 4))
        else:
            nuevo=CuentaAhorros.creando_cuenta_ahorro(self,monto)
            with open('intereses_deposito.json', 'r') as f:
                diccionario=json.loads(f.read())
            nuevo=nuevo.__dict__
            diccionario.append(nuevo)
            with open('intereses_deposito.json','w') as f:
                f.write(json.dumps(diccionario, indent= 4))            


    def calculo_de_interes_retiro(self,monto,instruccion='none'):
        if instruccion=='actualizar':
            with open('intereses_retiro.json', 'r') as f:
                diccionario=json.loads(f.read())
            with open('configuracion.cfg.json', 'r') as f:
                porcentaje=json.loads(f.read())
            taza_interes=porcentaje["tasaInteres"]
            for i in diccionario:
                i["_CuentaAhorros__interes_ganado"]+=i["_Cuenta__saldo"]*(taza_interes/100)*(1/360)
            with open('intereses_retiro.json','w') as f:
                f.write(json.dumps(diccionario, indent= 4))

        else:
            nuevo=CuentaAhorros.creando_cuenta_ahorro(self,monto)
            with open('intereses_retiro.json', 'r') as f:
                diccionario=json.loads(f.read())
            nuevo=nuevo.__dict__
            diccionario.append(nuevo)
            with open('intereses_retiro.json','w') as f:
                f.write(json.dumps(diccionario, indent= 4))

    # def obtener_cuenta_ahorro()
if __name__ == '__main__':

    k=Cuenta('98','139398',0)
    k.guardar_cuenta()
    print(k.obtener_datos_cuenta())
    print(f'-----------------------------LA CUENTA K REALIZO UN DEPOSITO--------------------------------------')

    k.deposito(100000)
    j=CuentaAhorros.calculo_de_interes_deposito(k,100000)

    print(f'-----------------------------LA CUENTA K REALIZO UN RETIRO--------------------------------------')

    k.retiro(10000)
    h=CuentaAhorros.calculo_de_interes_retiro(k,10000)
    print(f'-----------------------------REALIZAMOS LOS AJUSTES DE INTERESES POR 10 DIAS--------------------------------------')
    for i in range(10):
        CuentaAhorros.calculo_de_interes()
        time.sleep(2)
    print(f'-----------------------------REALIZAMOS LOS AJUSTES DE INTERESES POR 349 DIAS--------------------------------------')

    for i in range(349):
        CuentaAhorros.calculo_de_interes()

    print(f'-----------------------------AL SIGUIENTE DIA, SE ACREDITA A LAS CUENTAS SUS RESPECTIVOS INTERESES----------------------------')   

    input('esta listo?')
    CuentaAhorros.calculo_de_interes()

    print(k.obtener_datos_cuenta())


    
    print(f'-----------------------------IMPRIMIENDO INTERESES----------------------------')       

    CuentaAhorros.mostrar_intereses(k)