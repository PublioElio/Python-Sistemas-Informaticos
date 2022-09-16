"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este programa pregunta al usuario si quiere hacer calcular el área de un triángulo o la de un círculo.
Para el primer caso el programa pide la base y la altura y muestra el área.
Para el caso del cálculo del área de un círculo, el programa solicita el radio y muestra el área.
"""
import math  # he importado math porque usaremos pi para calcular el área del círculo


def calculatetriangle():  # función que calcula el área de un triángulo
    height = input("Introduzca la altura: ")
    height = float(height)
    width = input("Introduzca la base: ")
    width = float(width)
    area = (height*width)/2
    print("El área del triángulo es: ", area)


def calculatecircle():  # función que calcula el área de un círculo
    radius = input("Introduzca el radio: ")
    radius = float(radius)
    area = math.pi*(radius**2)
    print("El área del círculo es: ", area)


def askuser():  # función que pregunta al usuario si quiere calcular un círculo o un triángulo
    print("""
    Este programa calculará el área de un triángulo o de un círculo.
    """)
    shape = input("Escriba la palabra círculo o triángulo: ")
    shape = shape.casefold()  # pasamos la palabra a minúsculas
    if shape == "triángulo" or shape == "triangulo":
        calculatetriangle()
    elif shape == "círculo" or shape == "circulo":
        calculatecircle()
    else:
        print("Por favor, introduzca una palabra válida.")  # en caso de que se equivoque, volvemos a preguntar
        askuser()


askuser()
