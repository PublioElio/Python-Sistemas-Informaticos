"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa imprime por pantalla todas las potencias de dos
menores o iguales a 2048
"""


def printpowers():  # función que imprime las potencias de 2 hasta 2048
    introductorytext = """
    Las siguientes son todas las 
    potencias de 2 hasta 2048
    """
    print(introductorytext)

    limit = 2048  # esta variable marcará el límite
    i = 0  # esta variable es el índice
    powers = 2**i  # esta variable son las potencias de 2

    while powers <= limit:
        print(powers)
        i += 1  # sumo uno al índice
        powers = 2**i  # elevo dos al índice


printpowers()
