"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide dos números enteros al usuario escriba si el mayor es múltiplo del menor
"""


def askfornumbers():  # función para crear la listofnumbers de números y ordenarlos
    print("""
    Introduzca dos números enteros y el programa le dirá
    si el mayor es múltiplo del menor
    """)
    numberslist = []
    firstnumber = input("Introduzca el primer número: ")
    firstnumber = int(firstnumber)
    secondnumber = input("Introduzca el segundo número: ")
    secondnumber = int(secondnumber)
    if firstnumber > secondnumber:
        numberslist.append(firstnumber)
        numberslist.append(secondnumber)
    else:
        numberslist.append(secondnumber)
        numberslist.append(firstnumber)
    return numberslist


def checknumbers(numberlist):  # función para resolver si el número menor es múltiplo del menor
    if numberlist[0]%numberlist[1] == 0:
        print("El número", numberlist[1], "es múltiplo de", numberlist[0])
    else:
        print("El número", numberlist[1], "no es múltiplo de", numberlist[0])


usernumbers = askfornumbers()

checknumbers(usernumbers)
