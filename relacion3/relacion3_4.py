"""
ejercicios de Python III Sistemas Informáticos

Autor: Adriano Díaz

Este programa pide al usuario una cadena
Luego le solictita qué caracteres quiere
imprimir en pantalla e imprime solo los pares
"""
introductoryText = """
   Introduzca una cadena de caracteres y después diga 
   cuántos caracteres de la misma quiere imprimir por pantalla
   se imprimirán solo los pares:
   """


def askuserstring():  # este método solicita una palabra al usuario
    userstring = input(introductoryText)
    return userstring


def askposition(userstring):  # este método solicita un número de caracteres al usuario para sacar de la cadena
    number = input("Introduzca la cantidad de caracteres que \n"
                   "quiere extraer de la cadena: ")
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
    # a continuación se queda con los caracteres pares del rango introducido por el usuario
    substring = userstring[1:userposition:2]
    return substring


phrase = askuserstring()

position = askposition(phrase)

characters = searchposition(phrase, position)

print("En la cadena de caracteres '", phrase,
      "'\nlos caracteres pares en el rango introducido son: ", characters)
