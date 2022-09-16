"""
ejercicios de Python II Sistemas Informáticos

Autor: Adriano Díaz

Este programa lee una cadena de texto introducida por el usuario
y para cada letra indica si es una vocal o una consonante, además las guarda en una listofnumbers
y cuenta el total.
"""
vowels = "aeiou"  # defino la cadena de caracteres que forman las vocales


def get_user_phrase():  # método para pedir palabras al usuario
    phrase = input("Por favor, introduzca una frase: ")

    """ paso la frase a minúsculas y la siguiente orden
    es para quedarme solo con caracteres alfanuméricos """

    phrase = phrase.lower()
    phrase = "".join(character for character in phrase if character.isalpha())
    return phrase


def get_vowels(phrase):  # método para quedarse con las vocales
    return [character for character in phrase if character in vowels]


def get_consonants(phrase):  # método para quedarse con las consonantes
    return [character for character in phrase if character not in vowels]


text = get_user_phrase()
totalvowels = get_vowels(text)
totalconsonants = get_consonants(text)

print("Hay un total de ", len(totalvowels), "vocales en la palabra", text, "y son las siguientes: ", totalvowels)
print("Hay un total de ", len(totalconsonants), "consonantes en la palabra", text,
      "y son las siguientes: ", totalconsonants)
