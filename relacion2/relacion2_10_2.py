"""
Esta es otra versión del ejercicio
para realizar el factorial de un número
"""


def askusernumber():  # función para pedir al usuario el número
    number = int(input("Introduzca un número: "))
    return checknumber(number)


def checknumber(number):  # en esta función compruebo que el usuario no haya introducido un número menor de 0
    if number < 0:
        print("No es posible realizar el factorial de ", number, "\nIntroduzca un número mayor.")
        askusernumber()
    return number


def calculatefactorial(number):  # función para realizar el factorial
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    print(factorial)


usernumber = askusernumber()

calculatefactorial(usernumber)
