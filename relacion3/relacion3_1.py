"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa dice al ususario el
tamaño de una cadena introducida
"""
introductoryText = """
   Introduzca una cadena de caracteres 
   y este programa le dirá el tamaño de la misma:
   """


def askuserstring():
    userstring = input(introductoryText)
    userstring = userstring.lower()
    userstring = ''.join(character for character in userstring if character.isalpha())
    return userstring


phrase = askuserstring()

totalcharacters = len(phrase)

print("El número total de caracteres alfabéticos de esta cadena es: ", totalcharacters)
