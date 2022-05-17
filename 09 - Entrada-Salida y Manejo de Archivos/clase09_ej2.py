'''
import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 2:
    from datetime import datetime
    import os
    marca_de_tiempo = datetime.now()
    marca_de_tiempo = int(datetime.timestamp(marca_de_tiempo))

    #temperatura = sys.argv[1]
    #humedad = sys.argv[2]
    lluvia = sys.argv[1]
    temperatura = input('Ingrese la temperatura en grados centígrados')
    humedad = input('Ingrese el porcentaje de humedad')
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    logs_lluvia = open('clase09_ej2.csv', 'a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')
'''

'''
import sys

if (len(sys.argv) == 2):

    from datetime import datetime
    import os

    #datos solicitados al usuario
    llovio = sys.argv[1]
    temperatura = input("Ingrese el valor de la temperatura:")
    humedad = input("Ingrese el valor de la humedad:")

    #marca de tiempo
    date = datetime.now()
    date = int(datetime.timestamp(date))

    #informacion total
    info = str(date)+","+temperatura+","+humedad+","+llovio

    #Pasarlo a un csv
    csv = open("clase09_ej2.csv",'a')
    csv.write(info+"\n")
    csv.close()

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')
'''

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
