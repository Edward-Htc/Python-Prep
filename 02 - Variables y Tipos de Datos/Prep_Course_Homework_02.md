## Variables

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
    a = 12
    print(a)

2) Imprimir el tipo de dato de la constante 8.5
    type(8.5)

3) Imprimir el tipo de dato de la variable creada en el punto 1
    type(a)

4) Crear una variable que contenga tu nombre
    mi_nombre = "edward huarcaya tacas"

5) Crear una variable que contenga un número complejo
    complex = 4 + 4j

6) Mostrar el tipo de dato de la variable crada en el punto 5
    type(complex)

7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
    pi = 3.1416

8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
    var1 = True
    var2 = "True"
    var1 == var2

9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
    print("el tipo de variable 1 es "+type(var1)+", el tipo de variable 2 es "+type(var2))

10) Asignar a una variable, la suma de un número entero y otro decimal
    var10 = 3 + 1.2

11) Realizar una operación de suma de números complejos
    var11 = 2 + 4j
    var11_ = 3+ 3j
    var 11_1 = var11 + var11_

12) Realizar una operación de suma de un número real y otro complejo
    var12 = 2 + (4 + 3j) 

13) Realizar una operación de multiplicación
    var13 = 3 * 2

14) Mostrar el resultado de elevar 2 a la octava potencia
    print(2**8)

15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
    q = 27 / 4
    print(q)

16) De la división anterior solamente mostrar la parte entera
    print(27//4)  
    ## 3

17) De la división de 27 entre 4 mostrar solamente el resto
    print(27 % 4)
    ## 6

18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
    result = 4*6 + 3

19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
    alfa1 = "alfanumerico 1"
    alfa2 = "alfanumerico 2"
    print(alfa1 + alfa2)

20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
    "2" == 2

21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
    int("2") == 2

22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
    ## No se puede convertir una variable de tipo string a float

23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
    var1 = 3
    var2 = 2
    var1 -= var2

24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
    result = 4
    ## realiza un desplazamiento a la izquierda de bit a bit.
    ## El sistema de numeracion binario es una tecnica de numeracion donde solo se usan 2 numeros, el 0 y 1.

25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
    int(2) + int('2')
    float(2) + float('2')
    string(2) + string('2')
    ## La conversion a string concatenaria los dos valores resultando '22' y no resultaria 4 como es el caso de la operacion suma

26) Realizar una operación válida entre valores de tipo entero y string
    nombre = "edward huarcaya"
    repetir = 3
    print(nombre*repetir + "se repite "+str(repetir)+" veces")
    