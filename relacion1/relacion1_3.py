"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este Programa solicita al usuario que introduzca por teclado dos números
y le dice cuál es el mayor de los dos, o si ambos son iguales
"""


def comparenumbers(number_list):  # este método compara los dos primeros elementos de la listofnumbers de números
    if number_list[0] > number_list[1]:
        print("El número mayor es: ", number_list[0])
    elif number_list[0] == number_list[1]:
        print("Ambos números son iguales")
    else:
        print("El número mayor es: ", number_list[1])


def askfornumbers():  # este método pide al usuario dos números y los mete en una listofnumbers
    print("""
    Por favor, introduzca a continuación dos números.
    El programa le dirá cúal de ellos es mayor, o si son iguales.
    """)
    number_list = []
    number1 = input("introduzca el primer número:")
    number_list.append(number1)
    number2 = input("introduzca el segundo número:")
    number_list.append(number2)
    return number_list


user_numbers = askfornumbers()

comparenumbers(user_numbers)
