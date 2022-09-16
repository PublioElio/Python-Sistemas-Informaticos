"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa solicita al usuario dos números y calcula la división
del mayor entre el menor mediante restas sucesivas.
"""


def askforparameters():  # función para pedir parámetros de entrada al usuario
    parameters = []  # inicializo la listofnumbers donde irán los parámetros del programa
    introductorytext = """
    Introduzca dos números enteros y el programa
    realizará la división mediante restas sucesivas.
    El divisor no puede ser cero:
    """
    print(introductorytext)
    divisor = input("Introduzca el divisor: ")
    divisor = int(divisor)  # convertimos la variable divisor en int
    verifydivisor(divisor)
    parameters.append(divisor)
    dividend = input("Introduzca el dividendo: ")
    dividend = int(dividend)  # convertimos la variable dividend en int
    parameters.append(dividend)
    parameters.sort()  # ordeno la listofnumbers para que siempre vaya el menor en el lugar 0
    return parameters


def verifydivisor(divisor):  # esta función comprueba que el divisor no sea cero
    if divisor == 0:
        print("El divisor debe ser distinto de cero.")  # enviamos un mensaje de error al usuario
        askforparameters()


def makedivision(parameters):  # esta función recibe la listofnumbers y realiza la división por restas
    quotient = 0
    while parameters[1] > 0:
        parameters[1] = parameters[1] - parameters[0]
        quotient += 1
    return quotient


division = askforparameters()

result = makedivision(division)

print("El resultado de la división es: ", result)
