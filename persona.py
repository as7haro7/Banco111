import json

class persona:
    def __init__(self,codigo_cliente, nombres, apellidos, cedula_identidad, direccion, referencia):
        self.__codigo_cliente = codigo_cliente
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__cedula_identidad = cedula_identidad
        self.__direccion = direccion
        self.__referencia = referencia

#---------------------GETERS-------------------------------------

    def get_codigo_cliente(self):
        return print(self.__codigo_cliente)
    
    def get_nombres(self):
        return print(self.__nombres)
    
    def get_apellidos(self):
        return print(self.__apellidos)
    
    def get_cedula_identidad(self):
        return print(self.__cedula_identidad)
    
    def get_direccion(self):
        return print(self.__direccion)
    
    def get_referencia(self):
        return print(self.__referencia)


#------------------------SETERS--------------------------------        
                        
    def set_nombres(self,new):
        new=formato_de_nombre(new)
        self.__nombres = new
        
    def set_apellidos(self,new):
        new=formato_de_nombre(new)
        self.__apellidos = new
        
    def set_cedula_identidad(self,new):
        self.__cedula_identidad = new
        
    def set_direccion(self,new):
        self.__direccion = new
        	
    def set_referencia(self,new):
        self.__referencia = new
        	
    def set_codigo_cliente(self):        	
        code_cliente = next(generador_code_cliente)
        self.__codigo_cliente=code_cliente

        	        	
def generar_codigo_cliente():
    ini=11111
    while True:
        yield ini
        ini+=1        	
        	
generador_code_cliente = generar_codigo_cliente()

def formato_de_nombre(n):
    n = n.lower().split()
    nombre=''
    if len(n)==0: return False
    for a in n:
        nombre+=a[0].upper()+a[1:]+' '
    return nombre.strip()
        	        	
if __name__=='__main__':
    carlo=persona('123','pepepepe','perez gomez','1345678','av.viva','322322')
    carla = persona("1002", "Carla", "Gomez", "322322", "Av. Angeles", "Cerca Banco Sol")



    try:        
        with open('Base_de_datos.json', 'r') as f:
            diccionario=json.load(f)
    except FileNotFoundError:
        diccionario = {}

   



    lista = carlo.__dict__
    diccionario.append(lista)

    with open('Base_de_datos.json', 'w') as f:
        f.write(json.dumps(diccionario, indent= 4))

    with open('Base_de_datos.json', 'r') as f:
        diccionario=json.loads(f.read())

    cont=0
    for i in diccionario:
        cont+=1

    print(cont)
    carlo.set_codigo_cliente()
    carlo.get_codigo_cliente()
    carlo.set_nombres('carlos maRio')
    carlo.get_nombres()
