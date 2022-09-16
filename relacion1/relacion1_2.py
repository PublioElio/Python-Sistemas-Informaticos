"""
ejercicios de Python I Sistemas Informáticos

Autor: Adriano Díaz

Este Programa solicita al usuario que introduzca por teclado una nota numérica
y devuelva su equivalente en calificación literal según el siguiente criterio:
<5 - Insuficiente
<6 - Suficiente
<7 - Bien
<9 - Notable
>=9	- Sobresaliente
"""


def askforscore():  # esta función solicita al usuario una nota numérica
    score = input("Escriba la calificación obtenida: ")
    score = int(score)
    return score


def turnscoreintotext(score):  # esta función convierte el valor numérico en un string
    if score < 5:
        score = "Insuficiente"
    elif 5 >= score < 6:
        score = "Suficiente"
    elif 6 >= score < 7:
        score = "Bien"
    elif 7 >= score < 9:
        score = "Notable"
    elif score >= 9:
        score = "Sobresaliente"
    return score


userscore = askforscore()

userscore = turnscoreintotext(userscore)

print("La nota obtenida es un", userscore)  # aquí informo al usuario de la nota obtenida
