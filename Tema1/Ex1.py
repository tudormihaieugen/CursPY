"""
Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de caractere de tip string sau un sir de numere.
    Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de caractere a fost gasit de Alexandra”,
    unde Alexandra reprezinta numele vostru preluat automat de la tastatura.
In cazul in care valoarea este un sir de numere afisati pe ecran mesajul “Sirul de numere a fost gasit de Alexandra”,
    unde Alexandra reprezinta numele vostru preluat automat de la tastatura.
"""

sir = input("Introduceti un sir: ")

if sir.isdigit():
    sir = int(sir)
    print("Sirul de numere", sir, "a fost gasit de Mihai")
else:
    print("Sirul de caractere", sir, "a fost gasit de Mihai")
