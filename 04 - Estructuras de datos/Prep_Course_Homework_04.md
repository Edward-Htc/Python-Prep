## Estructuras de Datos

1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
    list1 = ['Peru','Argentina','Bolivia','Chile','Colombia','Brazil']
    print(list1)

2) Imprimir por pantalla el segundo elemento de la lista
    print(list1[1])

3) Imprimir por pantalla del segundo al cuarto elemento
    print(list1[1:4])

4) Visualizar el tipo de dato de la lista
    print(type(list1))

5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
    print(list1[3:])

6) Visualizar los primeros 4 elementos de la lista
    print(list1[:4])

7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
    ciudad = "Mexico"
    if(ciudad in list1):
        print("La ciudad ya existe")
    else:
        list1.append(ciudad)
        print("Se agrego la ciudad "+ciudad)
    

8) Agregar otra ciudad, pero en la cuarta posición
    list1.insert(3,"Uruguay")

9) Concatenar otra lista a la ya creada
    list2 = ["Francia","Italia","Alemania"]
    list1.extend(list2)
    print(list1)

10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
    print(list1.index('Uruguay'))

11) ¿Qué pasa si se busca un elemento que no existe?
    print('Venezuela' in list1)

12) Eliminar un elemento de la lista
    list1.remove("Chile")

13) ¿Qué pasa si el elemento a eliminar no existe?
    list1.remove("Cuba")
    #sale un error por que no encontro lo solicitado

14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
    var = list1.pop()
    print(var)

15) Mostrar la lista multiplicada por 4
    print(list1*4)

16) Crear una tupla que contenga los números enteros del 1 al 20
    tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

17) Imprimir desde el índice 10 al 15 de la tupla
    print(tup[10:15])

18) Evaluar si los números 20 y 30 están dentro de la tupla
    print(20 in tup)
    print(30 in tup)

19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
    var = "Paris"
    if(var in list1):
        print("ya existe")
    else:
        list1.append(var)
        print("se agrego "+var)
    
20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
    print(tup.count(2))
    print(tup.count(4))

21) Convertir la tupla en una lista
    temp = list(tup)
    print(type(temp))

22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
    var1,var2,var3 = tup[:3]

23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
    dicc = {
        "Pais" : list1 ,
        "Numeros" : tup,
        "Ciudad" : "Lima",
    }
    print(dicc)

24) Imprimir las claves del diccionario
    print(dicc.keys())

25) Imprimir las ciudades a través de su clave
    print(dicc["Ciudad"])