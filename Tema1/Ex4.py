"""
Creati un program in care utilizatorul sa introduca un numar.
Calculati daca numarul este pozitiv, zero sau negativ.
In cazul in care este pozitiv validati daca este mai mic decat 10 si afisati un mesaj de confirmare..
Daca numarul este zero afisati “Numarul este 0”,
    iar daca numarul este negativ atunci transformati numarul in numar pozitiv si afisati numarul pozitiv.
"""

nr = input("Dati un numar: ")

if nr.lstrip('-+').isdigit():
    nr = int(nr)
elif "." in nr:
    a = nr.split('.')
    if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
        nr = float(nr)
else:
    print("Nu ati introdus un numar")
    exit()

if nr > 0:
    print("Numarul introdus:", nr, "este pozitiv.")
    if nr < 10:
        print(nr, "este mai mic decat 10.")
    else:
        print(nr, "este mai mare decat 10.")
elif nr == 0:
    print("Numarul este 0")
else:
    print("Numarul introdu:", nr, "este negativ.")
    print("Modulul sau este:", -nr)
