"""
Creati un program in care utilizatorul sa introduca un numar.
Calculati daca numarul este pozitiv, zero sau negativ.
In cazul in care este pozitiv validati daca este mai mic decat 10 si afisati un mesaj de confirmare..
Daca numarul este zero afisati “Numarul este 0”,
    iar daca numarul este negativ atunci transformati numarul in numar pozitiv si afisati numarul pozitiv.
"""

nr = input("Dati un numar: ")

if nr.lstrip('-+').isdigit():
    if nr[0] == "-":
        print("Numarul modificat este:", -int(nr))
elif "." in nr:
    a = nr.split('.')
    if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
        nr = float(nr)
else:
    print("Valoarea", nr, "nu este un numar")

