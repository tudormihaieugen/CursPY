"""
Creati un program care are ca scop un meniu.
Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5 captat intr-o variabila.
Prezentati prin afisare acest sir de caractere:
     1 – Afisare lista de cumparaturi
     2 – Adaugare element
     3 – Stergere element
     4 – Stergere lista de cumparaturi
     5 - Cautare in lista de cumparaturi
Apoi folosindu-va de o constructie if-elif-else afisati:
- daca utilizatorul scrie de la tastaura 1 afisati “Afisare lista de cumparaturi”
- daca utilizatorul scrie de la tastaura 2 afisati “Adugare element”
- daca utilizatorul scrie de la tastaura 3 afisati “Stergere element”
- daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Cautare element”
- daca utilizatorul scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
"""

lista = []

while True:
    print("""
        1 – Afisare lista de cumparaturi
        2 – Adaugare element
        3 – Stergere element
        4 – Stergere lista de cumparaturi
        5 - Cautare in lista de cumparaturi
        0 - Oprire meniu
        """)
    a = input("Alegeti o optiune: ")

    if a == "1":
        print("1 - Afisare lista de cumparaturi: ")
        print(lista)
    elif a == "2":
        element = input("2 - Adaugati elementul: ")
        lista.append(element)
    elif a == "3":
        element = input("3 - Sterge elementul: ")
        if element in lista:
            print("Ati sters cu succes elementul: ", element, "de pe pozitia: ", lista.index(element))
            lista.remove(element)
        else:
            print("Elementul introdus nu se afla in lista")
    elif a == "4":
        print("4 - Stergere lista de cumparaturi")
        lista.clear()
        print("Ati sters cu succes lista de cumparaturi!")
    elif a == "5":
        print("Cautare in lista de cumparaturi")
        element = input("Elementul pe care doriti sa-l cautati: ")
        if element in lista:
            print("Elementul", element, "se afla in lista de cumparaturi pe pozitia: ", lista.index(element))
        else:
            print("Elementul", element, "nu se afla in lista de cumparaturi")
    elif a == "0":
        print("Sfarsit program!")
        break
    else:
        print("Alegerea nu exista. Reincercati.")
