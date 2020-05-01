"""
Creati un program in care utilizatorul sa introduca un an.
Calculati daca anul este bisect sau nu si afisati un raspuns in acest sens.
OBS: Un an bisect se imparte exact la 4 (fara rest).
"""

an = input("Dati un an: ")

if an.isdigit():
    an = int(an)
    if an % 4 != 0:
        print("Anul", an, "NU este bisect")
    elif an != 100:
        print("Anul", an, "este bisect")
    elif an != 400:
        print("Anul", an, "NU este bisect")
    else:
        print("Anul", an, "este bisect")
else:
    print("Nu ati introdus un numar intreg")
