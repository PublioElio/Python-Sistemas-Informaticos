"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide al usuario el año actual y un año cualquiera
y muestra cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
Si la diferencia es solo de un año, muestra un mensaje distinto al usuario
"""


def askforyears():  # esta función pregunta al usuario por el año en curso y otro cualquiera y los guarda en una listofnumbers
    print("A continuación, introduzca el año actual y otro cualquiera: ")
    listofyears = []
    firstyear = input("Introduzca el año actual: ")
    firstyear = int(firstyear)  # convierto en enteros el string que introduce el usuario
    listofyears.append(firstyear)
    secondyear = input("Introduzca el otro año: ")
    secondyear = int(secondyear)  # convierto en enteros el string que introduce el usuario
    listofyears.append(secondyear)
    return listofyears


def calculateyears(listofyears):  # esta función realiza el cálculo de años
    if listofyears[0] > listofyears[1]:
        difference = listofyears[0] - listofyears[1]
        if difference == 1:
            print("Eso fue el año pasado.")
        else:
            print("Han pasado", difference, "años desde entonces.")
    elif listofyears[1] > listofyears[0]:
        difference = listofyears[1] - listofyears[0]
        if difference == 1:
            print("Eso es el año próximo")
        else:
            print("Quedan", difference, "años para llegar a esa fecha.")
    else:
        print("Ambos años son el mismo")


useryears = askforyears()

calculateyears(useryears)
