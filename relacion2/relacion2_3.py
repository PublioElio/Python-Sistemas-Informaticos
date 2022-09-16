"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa muestra por pantalla las primeras 15 potencias de dos
"""
introductoryText = """
A continuación se muestran las
primeras 15 potencias de dos
"""
print(introductoryText)  # aquí doy información al usuario
powers = 0
number = 0
"""
for powers in range(16):
    number = 2**powers
    print(number)
"""
#  otra solución sería empleando una listofnumbers:
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in numberList:
    number = 2**i
    print(number)
