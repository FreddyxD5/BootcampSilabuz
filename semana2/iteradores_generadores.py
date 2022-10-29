#Funcion Generadora Ejemplo PPT
print("#EJEMPLO DEL PPT")
def funcion_generadora(l):
    """
    :param l: el ciclo for nos indica que "l" o es una tupla o es una sublista
            l1,l2  (l1,l2) | l1,l2  [l1,l2]
    """
    for l1, l2 in l:
        if l1 % 2 == 0:
            yield l1,l2+" Par"
        else:
            yield l1,l2+" NoPar"

lista1 = [4,8,11]
lista2 = ["a","b","c"]
for cont, (valor1, valor2) in enumerate(funcion_generadora(zip(lista1,lista2))):
    print(f"{cont} -> {valor1}: {valor2}")

print('------------')
for cont, (valor1, valor2) in enumerate(funcion_generadora([[1,"a"],[2,"b"],[3,"c"]])):
    print(f"{cont} -> {valor1}: {valor2}")

print(" ")
print("#PREGUNTA 1")
#TALLER ITERADORES Y GENERADORES
#PREGUNTA 1
"""
Dada la lista de notas [15,20,18] y la lista de
alumnos ["Marcelo", "José", "Juan"]
Imprimirlos de la siguiente forma:

Marcelo : 15
José : 20
Juan : 18
"""
lista_alumnos = ["Marcelo", "José", "Juan"]
lista_notas = [15,20,18]

#Usamos zip para combinar ambas listas,
#uso nombre y nota, porque sabemos que la funcion zip devuelve una
#tupla (("Marcelo",18),("Jose",20),("Juan",18)) y en cada iteracion
# obtendremos 2 valores es similar cuando hacemos a, b = 18, 20

for nombre, nota in zip(lista_alumnos,lista_notas):
    print(f"{nombre} : {nota}")

#PREGUNTA 2
"""
Dada la siguiente lista ['Hola', True, 5, 6.04]
Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04

"""
print("")
print("#PREGUNTA 2")
lista = ['Hola', True, 5, 6.04]
#Usamos la funcion enumerate
for indice, valor in enumerate(lista):
    print(f"{indice} -> {valor}")

#PRGUNTA3
"""
Dada la lista de notas [15,20,18]y la lista de
alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20
2 -> Juan : 18
3 -> Marcelo : 15
"""
print("")
print("#EJERCICIO 3")
for indice, (nombre, valor) in enumerate(sorted(zip(lista_alumnos, lista_notas)), start=1):
    print(f"{indice}->{nombre}: {valor}")


print("")
#PREGUNTA 4
"""
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:
Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}
Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}
"""
print("#EJERCICIO 4")
def generador_contar_palabras(palabra):
    #creamos un diccionario vacio, éste contendra las letras con su
    #respectivo valor
    dict = {}
    #iteramos la palabras
    for letra in palabra:
        #Si la letra ya esta en el diccionario sumamos 1
        if letra in dict:
            dict[letra] += 1
            # yield dict
        else:
            #si la letra no esta en el diccionario la creamos
            #y asignamos el valor de 1
            dict[letra] =  1
            # yield dict
    yield dict

#Sí queremos ver la iteracion de la palabra y como se va llenando el diccionario
#podemos descomentar los yields dentro de las condicionales

#Si pasamos una llave y un valor a un diccionario, éste lo creara en caso
#de que no exista.
#Las cadenas o string son iterables y pueden recorrerse en un for.
print("")
print("#EJERCICIO 4")
for valor in generador_contar_palabras("humanidad"):
    print(f"Para 'humanidad' : {valor}")

#PREGUNTA 5
"""
Teniéndos los siguientes criterios:

Desaprobado: nota < 11
Destacado: nota > 16
Aprobado: para el resto de casos

notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

Implementar registrar_aprobados como generador y que su único
parametro de entrada sea alumnos_notas Posteriormente utilizar un bucle y
enumerate para obtener la siguiente salida.
"""
#Necesitamos un generador, un generador tiene que tener la sentencia yield
#y esta funcion debe poder ejecutarse en un for

print("")
print("#EJERCICIO 5")

notas = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)
#Un generador tiene que tener la sentencia yield para que sea considerado como uno
def registrar_aprobados(alumnos_notas):
    for alumno, nota in alumnos_notas:
        if nota < 11:
            yield alumno, nota, " ( Desaprobado ) "
        elif nota < 16:
            yield alumno, nota, "( Aprobado )"
        else:
            yield alumno, nota, " (Destacado) "


#Como vamos a iterar y enumerar entonces si o si usaremos enumerate
#Tenemos nuestra funcion Generadora
#Ahora usamos el ciclo for para recorrerla

for indice, (alumno, nota, mensaje) in enumerate(registrar_aprobados(alumnos_notas), start=1):
    print(f"{indice}-> {alumno} : {nota} {mensaje}")
