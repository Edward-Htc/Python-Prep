## Variables

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
``` python
var = 2
print(var)
```
2) Imprimir el tipo de dato de la constante 8.5
``` python
print(type(8.5))
```
3) Imprimir el tipo de dato de la variable creada en el punto 1
``` python
type(var)
```
4) Crear una variable que contenga tu nombre
``` python
name = "edward huarcaya tacas"
```
5) Crear una variable que contenga un número complejo
``` python
comp = 4 + 8j
```
6) Mostrar el tipo de dato de la variable crada en el punto 5
``` python
print(type(comp))
```
7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
``` python
pi = 3,1416
```
8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
``` python
var1 = True
var2 = "true"
print(var1 == var2)
```
9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
``` python
print("el tipo de la variable 1 es "+type(var1)+" y el de la variable 2 es "+type(var2))
```
10) Asignar a una variable, la suma de un número entero y otro decimal
``` python
sum = 2 +1.3
```
11) Realizar una operación de suma de números complejos
``` python
sum_compl = 3 + 1j + 4 + 5j
```
12) Realizar una operación de suma de un número real y otro complejo
``` python
sum_t = 3 + 4 + 6j
```
13) Realizar una operación de multiplicación
``` python
multi = 2 * 4
```
14) Mostrar el resultado de elevar 2 a la octava potencia
``` python
print(2**8)
```
15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
``` python
var = 27/4
print(var)
```
16) De la división anterior solamente mostrar la parte entera
``` python
print(27//4)
```
17) De la división de 27 entre 4 mostrar solamente el resto
``` python
print(27%4)
```
18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
``` python
total = 6 * 4 + 3
```
19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
``` python
text1 = "hola"
text2 = "¿como estas?"
print(text1+text2)
```
20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
``` python
print(type("2") == type(2))
```
21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
``` python
print(type(int("2")) == type(int(2)))
```
22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
``` python
#no se puede convertir un string a float
```
23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
``` python
var = 3
var2 = 1
var -= var2
```
24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
``` python
print(1<<2)
```
25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
``` python
print(2 + '2')
#los tipos de datos no coinciden, por eso no esta permitido
#si fueran del mismo tipo no surgiria el error
```
26) Realizar una operación válida entre valores de tipo entero y string
``` python
lista = "hola"
print(lista*3)

```