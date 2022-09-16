"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide al usuario los coeficientes de
una ecuación de primer grado (a x + b = 0) y muestra la solución.
"""


def entercoefficients():  # este método solicita los coeficientes al usuario
    print("""
    Introduzca los coeficientes de una ecuación de primer grado
    y este programa la resolverá.
    """)
    coefficients = []
    a = input("Introduzca el valor de 'a': ")
    a = float(a)
    coefficients.append(a)
    b = input("Introduzca el valor de 'b': ")
    b = float(b)
    coefficients.append(b)
    return coefficients


def solveequation(coefficients):  # este método realiza el cálculo de la ecuación
    if coefficients[0] == 0 and coefficients[1] == 0:
        print("Todos los números son solución")
    elif coefficients[0] == 0 and coefficients[1] != 0:
        print("Esta ecuación no tiene solución")
    else:
        x = (coefficients[1]*-1)/coefficients[0]
        print("La solución es", x)


uservalues = entercoefficients()

solveequation(uservalues)
