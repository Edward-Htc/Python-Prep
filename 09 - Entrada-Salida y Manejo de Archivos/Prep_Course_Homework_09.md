## Entrada / Salida

1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos
``` python
        import sys

        if len(sys.argv) == 4:
        for i in sys.argv:
                print(i)
        else:
        print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
        print('Ejemplo: clase09_ej1.py 1 2 3')

```

2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.

``` python
        import sys
        from datetime import datetime

        if len(sys.argv) == 2:
        llovio = sys.argv[1]
        temperatura = input("Ingrese la temperatura:")
        humedad = input("Ingrese el valor de humedad:")

        ahora = datetime.now()
        marcador = int(datetime.timestamp(ahora))

        info = str(marcador)+','+temperatura+','+humedad+','+llovio

        file = open('clase09_ej2.csv','a')
        file.write(info+'\n')
        file.close()

        else:
        print("ERROR: Introdujo una cantidad de argumentos distinta de dos (2)")
        print('Ejemplo: clase09_ej1.py <llovio>')
```

Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*

``` python
import datetime

x = datetime.datetime.now()
print("Ahora =",x)
x = datetime.datetime(2020, 5, 10)
print("Fecha fija =",x)

fecha_hora = '2022-05-10 12:30:00'
objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
print("objeto datetime =", objeto_datetime)
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
print("timestamp =", marca_de_tiempo)
fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
print("fecha hora =", fecha_hora2)
``` 

3) Crear un archivo a partir de los datos presentes en el diccionario provisto. El cual debe contener en la primera fila el nombre de las claves y luego cada línea los elementos i-ésimos de las listas de valores contiguos y separados por coma ','. Este archivo debe llamarse clase09_ej3.csv

``` python
montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

file = open('clase09_ej3.csv','a')
cadena = ""
cont = 0
for i in montañas.keys():
        if(i != 'altura'):
                file.write(i+",")
        else:
                file.write(i+"\n")

while cont < len(montañas['pais']):
        file.write(montañas['nombre'][cont]+',')
        file.write(str(montañas['orden'][cont])+',')
        file.write(montañas['cordillera'][cont]+',')
        file.write(montañas['pais'][cont]+',')
        file.write(str(montañas['altura'][cont])+'\n')
        cont+=1
file.close()
```

4) Mostrar el tamaño en MB del archivo generado en el punto 3
``` python
print(str(round(os.path.getsize('clase09_ej3.csv')/1024,2)))
```
5) Crear una carpeta llamada clase09_montañas_altas
``` python
        os.makedirs('clase09_montañas_altas')
```

6) Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia **os.system**

``` python
os.system('copy clase09_ej3.csv clase09_montañas_altas')
```

7) Listar el contenido de la carpeta clase09_montañas_altas
``` python
os.listdir('clase09_montañas_altas')
```