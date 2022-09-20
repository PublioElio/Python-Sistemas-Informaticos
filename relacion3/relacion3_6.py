"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa implime en mayúscula los caracteres en las posciones múltiplos de tres
en una cadena introducida por el usuario
"""
introductoryText = """
   Introduzca una cadena de caracteres y este programa 
   mostrará en mayúsculas las posiciones múltiplos de tres:
   """


def askuserstring():  # este método solicita al usuario una cadena de al menos tres caracteres
    userstring = input(introductoryText)
    if len(userstring) < 3:
        print("Por favor, introduzca una cadena de, al menos, tres caracteres.")
        userstring = askuserstring()
    else:
        userstring = userstring.upper()
    return userstring


phrase = askuserstring()

print("en la cadena introducida, estos son los caracteres múltiplos de tres:")
print(phrase[0::3])

