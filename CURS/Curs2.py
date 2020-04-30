# #index string
# cuvant = 'abcde'
#
# print(cuvant[0])  #index 0
# print(cuvant[6:])  #fara : e eroare, cu : nu afiseaza nimic
# print(cuvant[-1])  #ultimul index
#
# for letter in cuvant:
#     print(letter)
#
# print(cuvant.replace('d', 'f'))  #afiseaza cuvantul modificat
# print(cuvant)  #afiseaza cuvantul nemodificat --> replace nu atribuie valoarea
#
# if "b" in cuvant:
#     print("da")
# print(cuvant.find('b'))  #afiseaza 1 = true, -1 = false
#
# print(cuvant.split("c"))  #split --> lista cu 2 string
# print("".join(cuvant.split("c")))  #lipeste cele 2 string-uri din lista rezultata

# #tuples - imutabil
# tuplu = (1)
# print(type(tuplu))  # --> int
# tuplu = (1, )
# print(type(tuplu))  # --> tuplu
#
# tuplu = tuplu + (2, 3, 4)  # --> concatenare
# print(tuplu)
