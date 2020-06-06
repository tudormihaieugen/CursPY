"""
• Creati o clasa ce va reprezenta un catalog de prajituri.
La crearea unui obiect al acestei clase vor solicita trei argumente reprezentand nume (sir de caractere), preț (integer)
    si gramaj (integer) cu care va crea trei atribute. Fiecare obiect creat va fi adaugat intr-o lista mentinuta de o variabila a clasei.
Clasa trebuie sa detina o metoda care sa poate afisa toate prăjituri sortand în funcție de gramaj afisand gramajul,
    numele și pretul Clasa trebuie sa detina o metoda care sa poate afisa toate prăjituri în funcție de pret afisand gramajul, numele și prețul
"""

class Catalog:
    list_nume = []
    list_pret = []
    list_gramaj = []

    def __init__(self, nume=' ', pret=0, gramaj=0):
        self.nume = nume
        self.list_nume.append(nume)
        self.pret = pret
        self.list_pret.append(pret)
        self.gramaj = gramaj
        self.list_gramaj.append(gramaj)

    def sortare_gramaj(self):
        n = len(self.list_gramaj)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if int(self.list_gramaj[j]) > int(self.list_gramaj[j + 1]):
                    self.list_gramaj[j], self.list_gramaj[j + 1] = self.list_gramaj[j + 1], self.list_gramaj[j]
                    self.list_nume[j], self.list_nume[j + 1] = self.list_nume[j + 1], self.list_nume[j]
                    self.list_pret[j], self.list_pret[j + 1] = self.list_pret[j + 1], self.list_pret[j]

        for k in range(len(self.list_gramaj)):
            print(f"{self.list_gramaj[k]} grame {self.list_nume[k]} {self.list_pret[k]} ron")

    def sortare_pret(self):
        n = len(self.list_nume)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if int(self.list_pret[j]) > int(self.list_pret[j + 1]):
                    self.list_pret[j], self.list_pret[j + 1] = self.list_pret[j + 1], self.list_pret[j]
                    self.list_gramaj[j], self.list_gramaj[j + 1] = self.list_gramaj[j + 1], self.list_gramaj[j]
                    self.list_nume[j], self.list_nume[j + 1] = self.list_nume[j + 1], self.list_nume[j]

        for k in range(n):
            print(f"{self.list_gramaj[k]} grame {self.list_nume[k]} {self.list_pret[k]} ron")

"""
• Creati a doua clasa care mosteneste prima clasa care se va numi tort.
 Aceasta clasa va avea un atribut numit etajat care default sa devina False și alt atribut care se numește glazura (sir de caractere) ce este default „ciocolata”. 
    Aceste atribute trebuiesc implementate printr-o metoda de setare cu parametrii de intrare. O alta metoda permite citirea acestora.
"""

class Tort(Catalog):
    def set_atr(self, etajat=False, glazura="ciocolata"):
        self.etajat = etajat
        self.glazura = glazura

    def get_atr(self):
        return self.etajat, self.glazura

"""
• Creati a treia clasa care mosteneste prima clasa care se va numi fursec. Aceasta va mosteni intocmai prima clasa fara a modifica/ adauga nimic.
"""

class Fursec(Catalog):
    pass

"""
Creati 3 obiecte ale clasei tort si trei obiecte ale clasei fursec.
Afisati prajiturie dupa gramaj.
Afisati prajiturie dupa pret.
Folositi pentru un obiect de tip tort modificarea atributelor etajat in True si glazura in “cacao”, apoi pentru acest
obiect folositi metoda de afisare a atributelor glazura si etajat.
De asemenea, folositi metoda de setare/afisare si pentru un alt obiect de tip tort
"""

prajitura1 = Tort("Cabana", 15, 4)
prajitura2 = Tort("Dobos", 12, 10)
prajitura3 = Tort("Fanta", 10, 6)

fursec1 = Fursec("Fursec cu ciocolata", 10, 5)
fursec2 = Fursec("Fursec cu vanilie", 12, 2)
fursec3 = Fursec("Fursec cu  stafide", 70, 4)

print("Sortare dupa gramaj:")
prajitura1.sortare_gramaj()
print("\nSortare dupa pret:")
prajitura1.sortare_pret()

prajitura1.set_atr(True, "cacao")
prajitura2.set_atr()
print("\nAtribute:")
print(f"{prajitura1.nume} {prajitura1.gramaj} grame {prajitura1.pret} ron etaj/glazura = {prajitura1.get_atr()}")
print(f"{prajitura2.nume} {prajitura2.gramaj} grame {prajitura2.pret} ron etaj/glazura = {prajitura2.get_atr()}")
