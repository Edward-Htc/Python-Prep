## Clases y Programación Orientada a Objetos

1) Crear la clase vehículo que contenga los atributos:<br>
Color<br>
Si es moto, auto, camioneta ó camión<br>
Cilindrada del motor

    class Vehiculo:
        def __init__(self,color,tipo,cilindrada):
            self.color = color
            self.tipo = tipo
            self.cilindrada = cilindrada

2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
Acelerar<br>
Frenar<br>
Doblar<br>

    class Vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada
        self.velocidad=0
        self.direccion=0

    def acelerar(self,vel):
        self.velocidad+=vel
    def frenar(self,vel):
        self.velocidad-=vel
    def doblar(self,grado):
        self.direccion += grado


3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

    v1 = Vehiculo('amarillo','auto',3)
    v2 = Vehiculo('rojo','moto',1)
    v3 = Vehiculo('rojo','camioneta',5)

    v1.acelerar(10)
    v2.acelerar(10)
    v3.acelerar(10)
    v1.frenar(3)
    v2.frenar(3)
    v3.frenar(3)
    v1.doblar(2)
    v2.doblar(1)
    v3.doblar(3)

4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

    class Vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada
        self.velocidad=0
        self.direccion=0

    def acelerar(self,vel):
        self.velocidad+=vel
    def frenar(self,vel):
        self.velocidad-=vel
    def doblar(self,grado):
        self.direccion += grado
    def estado(self):
        print("La velocidad: ",str(self.velocidad)," direccion: "+str(self.direccion))
    def detalles(self):
        print("Color: ",self.color," tipo: "+self.tipo," cilindrada: ",self.cilindrada)

v1 = Vehiculo('rojo', 'auto', 2)
v1.detalles()

v1.estado()
v1.acelerar(30)
v1.estado()

5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
Verificar Primo<br>
Valor modal<br>
Conversión grados<br>
Factorial<br>

class Metodos:
    def __init__(self):
        pass

    def factorial(self,numero):
        if(type(numero) != int):
            return "El dato debe de ser de tipo entero"
        if(numero <= 0):
            return "El numero debe de ser positivo mayor a cero"
        if(numero > 1):
            numero = numero * self.factorial(numero-1)
        return numero
    
    def conversion_grados(self,valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
        
    def esPrimo (self,numero):
        primo = True
        for i in range(2,numero+1):
            if(numero % i == 0 and i < numero):
                primo = False
                break
        return primo   
    
    def crearDicc(self,lista):
        diccionario = {}
        for i in lista:
            cantidad = 0
            cantidad = lista.count(i)
            if(not bool(diccionario) == True):
                diccionario[i] = cantidad
            elif(not(i in diccionario)):
                diccionario[i] = cantidad
        return diccionario

    def encontrarMayorRepetido(self,lista,opcion="mayor"):
        mayor = -999
        menor = 999
        clave = 0
        clave2 = 0
        diccionario = self.crearDicc(lista)
        for i in diccionario:
            if(mayor < diccionario[i]):
                mayor = diccionario[i]
                clave = i
            if(menor > diccionario[i]):
                menor = diccionario[i]
                clave2 = i
        if(opcion == "mayor"):
            return "el numero que mas se repite es el "+str(clave)+" con "+str(mayor)+" repeticiones"
        return "el numero que menos se repite es el "+str(clave2)+" con "+str(menor)+" repeticiones"


6) Probar las funciones incorporadas en la clase del punto 5

    m = Metodos()
    m.esPrimo(7)
    listado = [1,8,2,5,4,8,10,7]
    print(m.encontrarMayorRepetido(listado))
    m.conversion_grados(10, 'celsius', 'kelvin')
    m.factorial(6)



7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

    class Metodos:
    def __init__(self,lista):
        self.lista = lista
#-----------------------------------------------------
    def lista_Factorial(self):
        for i in self.lista:
            print(self.factorial(i))
    
    def lista_Conversion_grados(self,origen,destino):
        for i in self.lista:
            print(self.conversion_grados(i,origen,destino))

    def lista_esPrimo(self):
        for i in self.lista:
            print(self.esPrimo(i))
            
    def lista_Moda(self):
        print(self.encontrarMayorRepetido(self.lista))
#-----------------------------------------------------
    def factorial(self,numero):
        if(type(numero) != int):
            return "El dato debe de ser de tipo entero"
        if(numero <= 0):
            return "El numero debe de ser positivo mayor a cero"
        if(numero > 1):
            numero = numero * self.factorial(numero-1)
        return numero
    
    def conversion_grados(self,valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
        
    def esPrimo (self,numero):
        primo = True
        for i in range(2,numero+1):
            if(numero % i == 0 and i < numero):
                primo = False
                break
        return primo   
    
    def crearDicc(self,lista):
        diccionario = {}
        for i in lista:
            cantidad = 0
            cantidad = lista.count(i)
            if(not bool(diccionario) == True):
                diccionario[i] = cantidad
            elif(not(i in diccionario)):
                diccionario[i] = cantidad
        return diccionario

    def encontrarMayorRepetido(self,lista,opcion="mayor"):
        mayor = -999
        menor = 999
        clave = 0
        clave2 = 0
        diccionario = self.crearDicc(lista)
        for i in diccionario:
            if(mayor < diccionario[i]):
                mayor = diccionario[i]
                clave = i
            if(menor > diccionario[i]):
                menor = diccionario[i]
                clave2 = i
        if(opcion == "mayor"):
            return "el numero que mas se repite es el "+str(clave)+" con "+str(mayor)+" repeticiones"
        return "el numero que menos se repite es el "+str(clave2)+" con "+str(menor)+" repeticiones"

m = Metodos([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
m.lista_Conversion_grados('celsius','farenheit')
m.lista_esPrimo()
m.lista_Moda()
m.lista_Factorial()

8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

    from Metodos import *
    
    m2 = Metodos([1,1,2,3,5,6,8,8])
    m2.lista_Conversion_grados('celsius','farenheit')
    m2.lista_esPrimo()
    m2.lista_Moda()
    m2.lista_Factorial()
