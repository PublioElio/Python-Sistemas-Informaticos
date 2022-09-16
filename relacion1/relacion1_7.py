"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide tres números al usuario y escribe si son los tres iguales,
si hay dos iguales o si son los tres distintos.
"""


def askfornumbers():
    print("""
    Introduzca tres números y este programa 
    le dirá cuántos de ellos son iguales
    """)
    numbers = []
    number1 = input("Introduzca un número: ")
    number1 = int(number1)
    numbers.append(number1)
    number2 = input("Introduzca un número: ")
    number2 = int(number2)
    numbers.append(number2)
    number3 = input("Introduzca un número: ")
    number3 = int(number3)
    numbers.append(number3)
    return numbers


def checknumbers(numbers):
    if numbers[0] != numbers[1]:
        if numbers[1] != numbers[2]:
            if numbers[0] != numbers[2]:
                print("Los tres números son distintos")
            else:
                print("Hay dos números iguales")
        else:
            print("Hay dos números iguales")
    else:
        if numbers[0] != numbers[2]:
            print("Hay dos números iguales")
        else:
            print("Los tres números son iguales")


usernumbers = askfornumbers()

checknumbers(usernumbers)
