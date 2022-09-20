"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa busca una cadena dentro de otra cadena, ambas introducidas por el usuario:
"""
introductoryText = """
   Introduzca una cadena de caracteres:
   """


def askuserstring():  # este método solicita una cadena de caracteres al usuario
    userstring = input(introductoryText)
    return userstring


def searchinstring(userphrase, userword):
    if userphrase.find(userword) != -1:
        print(userphrase, "contiene la segunda cadena ", userword)
    else:
        print("dentro de ", userphrase, "no se encuentra ", userword)


phrase1 = askuserstring()

word1 = askuserstring()

searchinstring(phrase1, word1)
