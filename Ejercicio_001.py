"""
Ejercicio 001

Generar un ejemplo en lenguaje Python que permita leer la información de un archivo txt
#1. Solo se debe usar la librería estándar de Python (no instalar librerías adicionales).
#2. Leer la información del archivo informacion.txt
#3. El script generado debe imprimir de forma detallada la información de cada línea de archivo.
"""

archivo=open('informacion.txt', encoding='utf8')   #Abrir el archivo y asignarlo a una variable
linea=archivo.readline()                           #Obtener la primera linea del archivo y guardarla en una variable
while linea:                                       #Bucle while para imprimir y leer cada linea
    print(linea, end='')
    linea=archivo.readline()
archivo.close()                                    #Cerrar el archivo   



