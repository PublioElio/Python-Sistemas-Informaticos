"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa calcula el factorial de un número introducido por teclado.
"""
from math import factorial


def askfornumber():  # función para pedir parámetros de entrada al usuario
    introductorytext = """
    Introduzca el número al que desea realizar el factorial
    """
    print(introductorytext)
    number = input("Introduzca el número: ")
    number = int(number)
    return number


n = askfornumber()

print("El factorial es: ", factorial(n))
