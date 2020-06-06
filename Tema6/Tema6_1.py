"""
Creati o clasa ce va reprezenta un catalog:
• La initializare trebuie sa oferim doi parametrii de intrare nume si prenume Metoda de initializare creaza un atribut numit materii de tip dictionar nepopulat,
    dar si un atribut numit absente initializat la 0.
• Avem o metoda care afiseaza absente implementat cu __str__
• Avem o metoda care incrementeaza cu 1 nr. de absente
• Avem o metoda care sterge un nr. (exclusiv un numar - verifica) de absente dat (pentru cazurile in care avem o scutire medical) fara a deveni negativ
"""

class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def increment(self, numar):
        self.absente += numar

    def delete(self, numar):
        if numar > self.absente:
            numar = self.absente
        self.absente -= numar

    def __str__(self):
        return "Absente: " + str(self.absente)

"""
Creati a doua clasa numita Extensie1 care sa mosteneasca prima clasa. Clasa materii sa aiba 3 metode:
Prima metoda permite adaugarea prin doi parametrii de intrare a unui sir de caractere reprezentand materia si o lista reprezentand notele.
    Acesti parametrii de intrare sunt utilizati pentru a adauga o intrare in dictionarul atribut materii al obiectului current.
    Cheia este materia (sirul de caractere) si lista reprezinta value.
A doua metoda permite afisarea tuturor materiilor unui student.
A treia metoda permite afisarea materiilor si media aritmetica a fiecarei liste asociate pentru fiecare materie in parte.
    Verificati daca in lista sunt elemente de tip numar si ignorati alte valori.
"""

class Extensie1(Catalog):
    def add(self, materia, note):
        self.materii.update({materia: note})

    def afisare_materii(self):
        for key in self.materii:
            print(key)

    def afisare_totala(self):
        for key in self.materii:
            suma = 0
            nr = 0
            media = 0
            for value in self.materii[key]:
                try:
                    suma += int(value)
                    nr += 1
                except ValueError:
                    pass
            if nr != 0:
                media = suma/nr
            print(key, media)

"""
Verificari: 
• Creati 1 student numit Ion Roata 
• Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata 
• Stergeti doua absente prin metoda specificata 
• Creati al doilea student numit George Cerc 
• Modificati argumentul absente sa fie incrementat de 4 ori prin metoda creata 
• Stergeti doua absente prin metoda specificata 
• Afisati absentele fiecarui student 
• Adaugati materia ”Python” impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare student
• Adaugati materia ”Matematica” la al doilea student numit George Cerc si “Romana” pentru studentul numit Ion Roata 
    impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare student 
• Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materilor unui student. 
• Verificati ce materii si ce note mediate au studentii.
"""

student1 = Extensie1("Ion", "Roata")
student1.increment(3)
student1.delete(2)

student2 = Extensie1("George", "Cerc")
student2.increment(4)
student2.delete(2)

print(f"Absente {student1.nume} {student1.prenume}:")
print(student1)
print(f"Absente {student2.nume} {student2.prenume}:")
print(student2)

student1.add("Python", [7, 9, 5])
student2.add("Python", [8, 7, 7])
student1.add("Romana", [7, 9, 5])
student2.add("Matematica", [7, 9, 5])

print("\n" f"Materii {student1.nume} {student1.prenume}:")
student1.afisare_materii()
print("\n" f"Materii {student2.nume} {student2.prenume}:")
student2.afisare_materii()

print("\n" f"Materii si medii {student1.nume} {student1.prenume}:")
student1.afisare_totala()
print("\n" f"Materii si medii {student2.nume} {student2.prenume}:")
student2.afisare_totala()
