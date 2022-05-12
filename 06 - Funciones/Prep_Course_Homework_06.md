## Funciones

1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def esPrimo (numero):
    primo = True
    for i in range(2,numero+1):
        if(numero % i == 0 and i < numero):
            primo = False
            break
    return primo    

esPrimo(9)
2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def lista_primo(lista):
    newLista = []
    for i in range(0,len(lista)):
        if(esPrimo(lista[i])):
            newLista.append(lista[i])
    return newLista

completo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista_primo(completo))

3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
def crearDicc(lista):
    diccionario = {}
    for i in lista:
        cantidad = 0
        cantidad = lista.count(i)
        if(not bool(diccionario) == True):
            diccionario[i] = cantidad
        elif(not(i in diccionario)):
            diccionario[i] = cantidad
    return diccionario

def encontrarMayorRepetido(lista,opcion="mayor"):
    mayor = -999
    menor = 999
    clave = 0
    clave2 = 0
    diccionario = crearDicc(lista)
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

listae = [1,2,3,4,5,6,7,6,5,6]
print(encontrarMayorRepetido(listae))

4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def crearDicc(lista):
    diccionario = {}
    for i in lista:
        cantidad = 0
        cantidad = lista.count(i)
        if(not bool(diccionario) == True):
            diccionario[i] = cantidad
        elif(not(i in diccionario)):
            diccionario[i] = cantidad
    return diccionario

def encontrarMayorRepetido(lista,opcion="mayor"):
    mayor = -999
    menor = 999
    clave = 0
    clave2 = 0
    diccionario = crearDicc(lista)
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

listae = [1,2,3,4,5,6,7,6,5,6]
print(encontrarMayorRepetido(listae,"menor"))

5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
Fórmula 1	: (°C × 9/5) + 32 = °F<br>
Fórmula 2	: °C + 273.15 = °K<br>
Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conversion_grados(valor, origen, destino):
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

print('1 grado Celsius a Celsius:', conversion_grados(1, 'celsius', 'celsius'))
print('1 grado Celsius a Kelvin:', conversion_grados(1, 'celsius', 'kelvin'))

6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
metricas = ['celsius','kelvin','farenheit']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', metricas[i], 'a', metricas[j],':', conversion_grados(1, metricas[i], metricas[j]))

7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
def factorial(numero):
    if(type(numero) != int):
        return "El dato debe de ser de tipo entero"
    if(numero <= 0):
        return "El numero debe de ser positivo mayor a cero"
    if(numero > 1):
        numero = numero * factorial2(numero-1)
    return numero
print(factorial(3))
print(factorial(-2))
print(factorial(1.23))
print(factorial('6'))
