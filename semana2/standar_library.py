#PREGUNTA 1
"""
Escriba un programa en Python que acepte el perímetro de un círculo que escriba un usuario.
Finalmente el programa debe imprimir:

El valor de π con 7 decimales.
El valor del área de dicho círculo (con 3 decimales) así como el valor del radio de dicho círculo (con 2 decimales).
Pistas

En geometría, el área encerrada por un círculo de radio r es π*r^2.
Del módulo math obtenga el valor de π para los cálculos que requiera.
La letra griega π representa una constante, que es igual a la relación entre la circunferencia de cualquier círculo y su diámetro.
"""
from genericpath import isfile
from math import pi, cos, log,e

# perimetro = float(input("Ingrese el valor del perimetro del circulo: "))
#perimetro = 2 * pi * r
# radio = perimetro / (2*pi)
# area = pi*(radio**2)    

# print(f"El valor de pi con 7 decimales es: {pi:.7f}")
# print(f"El area del cirulo con 2 decimales es: {area:.2f}")



#PREGUNTA 2
"""
El presente ejercicio se enfoca en la manipulación de
fechasutilizando datetime (Documentación oficial)

Explore la documentación y escriba un programa Python
para mostrar la fecha y la hora actuales bajo los siguientes formatos de 
ejemplo (imaginando hoy fuese 10 de septiembre del 2022):

10-09-22
10-09-2022
Hoy día es Saturday
10~09~2022
10-09-2022 14:20:51

"""
import datetime
#parametros de datetime (año, mes, dia, hora, minutos, segundos,)
# now = datetime.datetime(2022,9,10,14,30,52)
# print(now.strftime("%d-%m-%y"))
# print(now.strftime("%d-%m-%Y"))
# print(f"hoy es {now.strftime('%A')}")
# print(now.strftime("%d~%m~%Y"))
# print(now.strftime("%d~%m~%Y %H:%M:%S"))

#PREGUNTA3

"""
Escriba un programa de Python para listar todos los archivos
en un directorio en Python. (por precaución que sea en una carpeta
temporal y que no contenga archivos importantes, coloque copias)
"""
import os

directorio_actual = os.getcwd()
print(directorio_actual)
carpeta = "directorio_temporal"
ruta = os.path.join(directorio_actual, carpeta)
print(os.listdir(ruta))
#La anterior linea devuelve ['carpeta_test', 'prueba.txt', 'prueba2.txt']
#os.listir(ruta_carpeta)

#Verificar si la carpeta tiene archivos y guardarlos en una lista
#os.listdir(ruta) devuelve una lista con el contenido de la carpeta como se ve anteriormente
# La condicion if evalua si es un archivo (file en ingles) con la funcion "isfile(ruta_del_archivo)"
# pero isfile necesita una ruta completa, actualmente ruta tiene el valor de
# ruta='C:\Users\{nombre_usuario}\Documents\Bootcamp silabuz\semana2'
# esta depende de donde hayas creado tus archivos. 
# bien tienes la ruta + los nombres de los archivos 
# concatenas ruta + item  y obtiene = C:\Users\{nombre_usuario}\Documents\Bootcamp silabuz\semana2\prueba.txt
# isfile solo retorna 2 valores True/False en caso de que sea un archivo
lista_de_archivos = [item for item in os.listdir(ruta) if isfile(os.path.join(ruta,item))]
print(lista_de_archivos)



#PREGUNTA 4
"""
Sin usar bibliotecas como pandas.
Generar un archivo local con el contenido del siguiente archivo:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Utilizando import csv

Calcular:
1. El promedio de edad.
2. La distribución del sexo (número de mujeres vs varones).
3. El número de sobrevivientes y fallecidos.
"""

import csv 
data_filaname = 'titanic.csv'
edades = []
sexos = []
sobrevivientes = []
with open(data_filaname, 'r') as archivo:
    data_archivo = csv.reader(archivo)
    #hacemos este next para omitir la primera linea ya que en esta se encuentran
    #los nombres de las columnas
    #PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    next(data_archivo)
    for data in data_archivo:
        _,survived,_,_,sex,age,_,_,_,_,_,_ = data
        sobrevivientes.append(survived)
        sexos.append(sex)
        edades.append(age)

#Promedio de edades
edades = [float(edad) for edad in edades if edad!='']
print(f"Promedio de edades: {sum(edades)/len(edades):.0f}")
#La distribución del sexo (número de mujeres vs varones).
print(f"Hay un total de: {sexos.count('female')} Mujeres")
print(f"Hay un total de: {sexos.count('male')} Hombres")
#El número de sobrevivientes y fallecidos.
print(f"Hay un total de {sobrevivientes.count('1')} sobrevivientes.")
print(f"Hay un total de {sobrevivientes.count('0')} fallecidos.")


#PREGUNTA 5
"""
Escriba un programa en Python para calcular el número de días entre dos fechas.
No es necesario que use inputs para el ingreso de las fechas.
"""
fecha_inicial = datetime.datetime(2022,5,18,15,50,20)
fecha_final = datetime.datetime(2022,9,10,14,30,52)
#Solo es una resta, simplemente tenemos que definir las fechas
# y el abs (absoluto) es para que no retorne un valor negativo.
print(abs(fecha_inicial-fecha_final))

#PREGUNTA 6
"""
Desarrolle un función que lea el archivo y que de la columna QuotaAmount,
calcule el promedio de los valores para luego retornarlo.
"""



def calcular_quota(filename):
    monto_cuota = []
    with open(filename, 'r') as archivo:
        data_archivo = csv.reader(archivo)
        #hacemos este next para omitir la primera linea ya que en esta se encuentran
        #los nombres de las columnas
        #PuotaAmount,StartDate,OwnerName,Username
        next(data_archivo)
        for data in data_archivo:
            #*_ omite los demas campos, es para evitar repetir "_,_,_" el * hace referencia a los argumentos
            # monto,_,_,_ = data
            monto,*_ = data
            monto_cuota.append(int(monto))

    
    return f"{sum(monto_cuota)/len(monto_cuota):.2f}"

print(calcular_quota("ejemplo.csv"))
            

#EJERCICIO 7
"""
Del ejercicio anterior cree dos pruebas unitarias (use unittest),
una que compare el valor de retorno con "146633.33" y el otro con "15000",
ambos test deben dar "Ok" como salida.
"""
import unittest

class test_csv(unittest.TestCase):
    def test_es_igual(self):
        amount = calcular_quota("ejemplo.csv")
        self.assertAlmostEquals(amount, 146633.33)
    def test_no_es_igual(self):
        promedio_de_quota = calcular_quota("ejemplo.csv")
        self.assertNotAlmostEqual(promedio_de_quota, 15000)



# if __name__ =='__main__':
#     unittest.main()


#EJERCICIO 8

"""
Obtenemos prácticas en una laboratorio de una universidad y nos solicitan
implementar de un paper la siguiente expresión matemática:

formula = sumatoria de cos(log (e*i))  i=1 9

e la constante de Euler
log es logaritmo
cos es el coseno
"""
resultado = 0
for i in range(1,10):
    resultado += cos(log(e*i))

print(resultado)

#EJERCICIO 9
"""
1.Recolectar los feriados del 2022.

2.Al ingresar una fecha inicial y días hábiles Generar un 
código que permita encontrar la fecha siguiente sin considerar fines
de semana (sábado y domingo) ni feriados.
"""
def fecha_anadiendo_dias_habiles(fecha_inicio, dias_agregar, festivos):
    dias_habiles_agregar = dias_agregar
    fecha_actual = fecha_inicio

    while dias_habiles_agregar > 0:
        fecha_actual += datetime.timedelta(days=1)
        dia_semana = fecha_actual.weekday()
        if dia_semana > 4:#Domingo-> 6 , Sabado->5
            continue
        if fecha_actual in festivos:
            continue
        dias_habiles_agregar -=1
    return fecha_actual

fecha_comienzo_string = "2022-10-17"
fecha_comienzo = datetime.datetime.strptime(fecha_comienzo_string,"%Y-%m-d")
feriados = ["2022-11-01", "2022-12-08","2022-12-24","2022-12-25","2022-12-31","2023-01-01"]

fechas_feriados = [datetime.datetime.strptime(fecha,"%Y-%m-%d") for fecha in feriados]
diferencia_de_dias = 10
fecha_resultado = fecha_anadiendo_dias_habiles(fecha_comienzo, diferencia_de_dias, feriados)
print(fecha_resultado)

