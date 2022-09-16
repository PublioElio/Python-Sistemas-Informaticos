"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide dos números al usuario, realiza una división
y muestra un mensaje diciendo si el resultado es o no exacto (resto cero)
"""


def askforparameters():  # función para pedir parámetros de entrada al usuario
    introductorytext = """
    Introduzca dos números enteros 
    y el programa le dirá si el resultado de la división es exacto.
    El divisor no puede ser cero:
    """
    print(introductorytext)
    divisor = input("Introduzca el divisor: ")
    divisor = int(divisor)  # convertimos la variable divisor en int
    verifydivisor(divisor)
    dividend = input("Introduzca el dividendo: ")
    dividend = int(dividend)  # convertimos la variable dividend en int
    result = dividend % divisor  # realizamos la división y nos quedamos con el resto
    # lo siguiente es un shorthand if en el que compruebo si el resto de la división es cero o no
    print("El resultado de la división es", result, ", el resultado es exacto") if result == 0 \
        else print("El resultado de la división es", result, ", el resultado no es exacto")


def verifydivisor(divisor):  # esta función comprueba que el divisor no sea cero
    if divisor == 0:
        print("El divisor debe ser distinto de cero.")  # enviamos un mensaje de error al usuario
        askforparameters()


askforparameters()
