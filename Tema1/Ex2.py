"""
Creati un program in care utilizatorul sa introduca un numar.
Validati daca acest numar este par sau impar si afisati un raspuns in acest sens.
"""

nr = input("Dati un numar: ")

if nr[0] == "-" and nr[1:].isdigit() or nr.isdigit():
    nr = int(nr)
    if nr % 2 == 0:
        print("Numarul", nr, "este par")
    else:
        print("Numarul", nr, "este impar")
else:
    print("Nu ati introdus un numar")
