"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa lee valores introducidos por el usuario
hasta que teclee un número par, utilizando un bucle while.
"""

number = 1  # declaro e inicializo la variable de modo que entre en el bucle

while number % 2 != 0:  # solo saldrá del while si el número es par
    print("""
    Introduzca un número entero, si es par, finalizará el programa
    """)
    number = input("Su número: ")  # le pido al usuario el número
    number = int(number)  # lo casteo a int

print(number,  " es un número par, finalizó el programa.")
