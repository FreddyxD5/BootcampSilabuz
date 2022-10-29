#PREGUNTA 1
"""
Implementar la función get_avg que calcule el promedio de una lista de números:
Asimismo implementar un decorador que permita imprimir los siguientes mensajes

Inicio del cálculo del promedio de la lista de números.
El cálculo ha finalizado.

Entre ambos mensajes debe realizarse el cálculo del promedio de números.
"""
#Decorador_avg
def decorador_avg(function):
    """
    :param function: funcion que ha sido decorada
    """
    def nueva_funcion(lista):
        """
        :param lista: lista de numeros pasados como argumentos
                        a la funcion que ha sido decorada
        """

        print("Inicio del calulo del promedio de la lista de números.")
        print(function(lista))
        print('El calculo ha finalizado')
        # Retornamos una cadena vacia de lo contrario sí
        # ejecutamos el codigo sin la sgte linea
        # mostrara None, debido a que estamos retornando la funcion "nueva_funcion"
        # y esta no tiene valor alguno entonces python asume como None.
        return ""
    #Retornamos la funcion "nueva_funcion"
    return nueva_funcion

@decorador_avg
def get_avg(lista):
    return sum(lista)/len(lista)

#La secuencia es
# 1.- Llamamos a la funcion get_avg([5,5,5,5,5])
# 2.- lo primero que se ejecuta es La funcion decoradora que
#     recibe como argumento una funcion
# 3.- la funcion decoradora implementa una funcion "nueva_funcion" en donde los argumentos
#      ([5,5,5,5,5]) de la funcion get_avg seran evaluados
# 4.- Como la funcion decoradora retorna "nueva_funcion" entonces se ejecuta
#      nueva function
# 5.- Se imprime el primer mensaje
# 6.- Se ejecuta la funcion get_avg([5,5,5,5])
# 7.- Se imprime el segundo mensaje
# 8.- retorna el valor de la funcion "nueva_funcion" que es una cadena vacia " "
# 9.- Fin del programa

print(get_avg([5,5,5,5,5]))

#PREGUNTA 2
"""
Escriba un programa que dada una entrada numérica por el usuario,
ingrese a una función que duplique el valor y sea retornado en forma de
string o cadena. Utilice tipos tanto para las variables como para las funciones.
"""

num_input = int(input("Ingrese un numero: "))

def duplicar_valor(num: int) -> str:
    return num*2

print(duplicar_valor(num_input))


#PREGUNTA 3
"""
Cree una función con anotaciones, que tome una palabra y
duplique sus letras y las retorne en una lista.

Ejemplo:
Ingrese una palabra: hola
Retorna: ['h','h','o','o','l','l','a','a']
"""

def duplicar_letras(palabra):
    """
    :param palabra: palabra es una cadena(string) y es un iterable
    """
    nueva_palabra = ""
    for letra in palabra:
        nueva_palabra += letra*2
    #Una cadena puede convertirse a una lista con el metodo list
    return list(nueva_palabra)

print(duplicar_letras("hola"))

#PRGUNTA 4
"""
Dada la función "calc_par_impar" que retorna un booleano, dependiendo si
el número ingresado es par o impar, cree un decorador que imprima que tipo
de número a recibido la función.
"""
def decorator_par_impar(funcion):
    """
    :param funcion: Funcion que ha sido decorada
    """
    def nueva_funcion(numero):
        """
        :param numero: la funcion recibe un numero y retorna un booleano,
                        es por eso que la evaluamos con un if directamente.
        """
        if funcion(numero):
            return "Es par"
        return "Es impar"
    return nueva_funcion

#Sigue la misma secuencia que el ejercicio 2
@decorator_par_impar
def calc_par_impar(numero):
    if numero % 2 == 0:
        return True
    return False


print(calc_par_impar(7))
print(calc_par_impar(20))


#PREGUNTA 5
"""
Cree una función decoradora deco1 que muestre el siguiente flujo,
para cualquier número ingresado, por ejemplo para el número 30:


Hola, estoy decorando esta función.
Ingresaste el número 30
Terminé de decorar

"""

def deco1(funcion):
    def nueva_funcion(numero):
        print("Hola, estoy decorando esta función")
        funcion(numero)
        print("Terminé de decorar")
        return ""
    return nueva_funcion

@deco1
def mostrar(n):
    print("Ingresaste el numero",n)

print(mostrar(30))
