from inspect import Traceback
from traceback import TracebackException


class Metodos:
    def __init__(self,lista):
        if(type(lista) != list):
            raise ValueError("El valor ingresado no es de tipo 'List' ") 
        else:
            self.lista = lista
#-----------------------------------------------------
    def lista_Factorial(self):
        fac = []
        for i in self.lista:
            fac.append(self.factorial(i))
        return fac
    
    def lista_Conversion_grados(self,origen,destino):
        valoresEsperados = ["farenheit","celsius","kelvin"]
        grad = []
        if(origen not in valoresEsperados or destino not in valoresEsperados):
            print("Se esperaba uno de los siguientes valores [farenheit,celsius,kelvin]")
        else:
            for i in self.lista:
                grad.append(self.conversion_grados(i,origen,destino))
        return grad

    def lista_esPrimo(self):
        prim = []
        for i in self.lista:
            prim.append(self.esPrimo(i))
        return prim
            
    def lista_Moda(self):
         return self.encontrarMayorRepetido(self.lista)
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
        try:
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

        except Exception:
            print("los datos ingresados no son validos")

        
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
            return [clave,mayor]
        return [clave2,menor]