## Flujos de Control

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
    var1 = 4
    if(var1 < 0 ):
        print("la variable es menor a cero)
    elif(var1 > 0):
        print("la variable es mayor a cero)
    else:
        print("la variable es igual a cero")

2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
    var2 = 23
    var3 = "edward"
    if (type(var2) == type(var3)):
        print("variables del mismo tipo")
    else:
        print("variables de diferentes tipo")

3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
    
    for i in range(1,21):
        if(i % 2 == 0)
            print("el "+str(i)+" es numero par")
        else:
            print("el "+str(i)+" es numero impar")

    cont = 1
    while(1 < 21):
        if(i % 2 == 0)
            print("el "+str(i)+" es numero par")
        else:
            print("el "+str(i)+" es numero impar")

4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
    for i in range(1,6):
        print("la potencia 3 del numero "+str(i)+" es "+str(i**3))


5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
    var5 = 6
    for i in range(1,var5+1):
        print("numero "+str(var5))

6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
    
    fact = 7
    n = fact - 1
    while(n >= 1):
        fact = n * fact
        n-=1
    print(fact)

7) Crear un ciclo for dentro de un ciclo while
    n = 1
    while(n < 5):
        print("while numero "+str(n))
        for i in range(1,5):
            print("--->for numero "+str(i))
        n+=1

8) Crear un ciclo while dentro de un ciclo for
    for i in range(1,6):
        print("for numero "+str(i))
        n=1
        while(n < 5):
            print("---> while numero "+str(n))
            n+=1

9) Imprimir los números primos existentes entre 0 y 30
    
    for i in range(2,10):
    primo = True
    n = 2
    while(n <= i):
        if(i % n == 0 and n < i):
            primo = False
        n+=1
    if(primo):
        print("el numero "+str(i)+" es primo")
    else:
        print("el numero "+str(i)+" no primo")

            
        
10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
    for i in range(2,10):
    primo = True
    n = 2
    while(n <= i):
        if(i % n == 0 and n < i):
            primo = False
            break
        n+=1
    if(primo):
        print("el numero "+str(i)+" es primo")
    else:
        print("el numero "+str(i)+" no primo")

11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
    cont = 0
    for i in range(2,10):
        primo = True
        n = 2
        while(n <= i):
            cont +=1
            if(i % n == 0 and n < i):
                primo = False
            n+=1
        if(primo):
            print("el numero "+str(i)+" es primo")
        else:
            print("el numero "+str(i)+" no primo")
    print("cantidad: "+str(cont))

12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
cont = 0
    for i in range(2,33):
            primo = True
            n = 2
            while(n <= i):
                cont +=1
                if(i % n == 0 and n < i):
                    primo = False
                # break
                n+=1
            if(primo):
                print("el numero "+str(i)+" es primo")
            else:
                print("el numero "+str(i)+" no primo")
    print("cantidad: "+str(cont))

    #Si crece

13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
    min = 100
    while(min <= 300):
        if(min % 12 != 0):
            continue
        print("numero "+str(min))    

14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

    op = "si"
    while(op == "si"):
        for i in range(2,20):
            primo = True
            n = 2
            while(n <= i):
                if(i % n == 0 and n < i):
                    primo = False
                n+=1
            if(primo):
                print("el numero "+str(i)+" es primo")
            else:
                print("el numero "+str(i)+" no primo")
            op = input("desea continuar")
            if(op == "no"):
                break

15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
    n = 100
    while(n <= 300):
        if(n % 6 == 0):
            print("el numero es "+str(n))
            break
        n+=1