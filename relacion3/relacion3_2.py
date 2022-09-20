"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide al usuario una cadena
Luego le solictita qué caracteres quiere
imprimir en pantalla desde el inicio de la misma
"""
introductoryText = """
   Introduzca una cadena de caracteres y después diga 
   cuántos caracteres de la misma quiere imprimir por pantalla:
   """


def askuserstring():  # este método solicita una palabra al usuario
    userstring = input(introductoryText)
    return userstring


def askposition(userstring):  # este método solicita un número de caracteres al usuario para sacar de la cadena
    number = input("Introduzca la cantidad de caracteres que quiere extraer de la cadena: ")
    number = int(number)

    # aquí controlo que el usuario introduzca un número válido
    if number > len(userstring):
        print("El número introducido es superior a la longitud de la palabra")
        askposition(userstring)
    elif number < 0:
        print("El número introducido no puede ser inferior a cero")
        askposition(userstring)
    return number


def searchposition(userstring, userposition):  # este método extrae una subcadena
    substring = userstring[:userposition]
    return substring


phrase = askuserstring()

position = askposition(phrase)

character = searchposition(phrase, position)

print("En la cadena de caracteres '", phrase,
      "'\nla posición introducida se corresponde con los caracteres: ", character)
