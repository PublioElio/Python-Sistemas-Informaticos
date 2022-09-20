"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide al usuario una cadena de al menos trece caracteres
luego imprime los últimos trece caracteres impares empezando desde el final
"""
introductoryText = """
   Introduzca una cadena de al menos trece caracteres y después se imprimirán los
   trece últimos caracteres, comezando desde el final:
   """


def askuserstring():  # este método solicita una palabra al usuario
    userstring = input(introductoryText)
    if len(userstring) < 13:
        print("Por favor, introduzca una cadena de caracteres de mayor longitud")
        userstring = askuserstring()
    return userstring


def printodds(userstring):  # este método extrae una subcadena
    substring = userstring[::-1]  # aquí le doy la vuelta a la cadena
    substring = substring[0::2]  # aquí me quedo con los caracteres impares
    substring = substring[::-1]  # le vuelvo a dar la vuelta a la cadena
    substring = substring[-13:]  # me quedo con los últimos trece caracteres
    return substring


phrase = askuserstring()

characters = printodds(phrase)

print("En la cadena de caracteres '", phrase,
      "'\nlos trece últimos caracteres impares son: ", characters)
