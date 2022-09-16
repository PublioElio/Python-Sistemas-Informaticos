"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa calcula si un año introducido por el usuario es bisiesto.
"""


def askforyear():  # función para preguntar al usuario por un año
    print("""
    Introduzca un año y este programa
    le dirá si es bisiesto.
    """)
    year = input("Introduzca un año: ")
    year = int(year)
    return year


def leapyear(year):  # función que calcula si un año es bisiesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("El año", year, "es bisiesto")
            else:
                print("El año", year, "no es bisiesto")
        else:
            print("El año", year, "es bisiesto")
    else:
        print("El año", year, "no es bisiesto")


useryear = askforyear()

leapyear(useryear)
