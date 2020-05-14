#tuplu -> tuple(var)
#set -> set(var)
#lista -> list(var)
#string -> str(var)

# #exemple string
# exemplu = "abcde"
# print(exemplu[0])
# print(exemplu.replace("c", "r"))
# print(exemplu)
# exemplu = exemplu.replace("c", "r")  #reatribuire
# print(exemplu)
# print(exemplu.find("r"))  #return -1 (fals)
# print(exemplu.find("c"))  #return 0 (adevarat)
#
# x = "sir de caractere"
# a = "_".join(x.split(' '))

# #exemple tuplu
# x1 = ()
# x = ('1', 2, '3', ('2', '4', 545))
# y = x + (11, 3)
# print(type(x), y)
# print(y[1])  #e indexabil, dar nu poate fi modificata valoarea
# a = (1,)  #tuplu cu virgula
# print(a, type(a))
# for item in x:  #iterabil
#     print(item)

# #liste
# x = [True, 1, '4']
# print(x[1])
# x[1] = 'a'  #e modificabil
# print(x)
# x.append(5)  #adaugare element cu append
# print(x)
# y = [1, 2, ['3', '4', 5], '6', '7']
# print(y[2][1])  #lista in lista
# print(y[1:])  #slicing
# print(y[1:4])  #pana la n+1
# print(y[::-1])  #invers
# print(y[::2])  #din 2 in 2
# print(y[1:6:2])  #de la 1 la 7 din 2 in 2
# print(y.index('6'))  #returneaza indexul
# print(y.count('7'))  #returneaza numarul de aparitii

# #set
# y = [1, 2, '6', '7', '7']
# print(set(y))  #scapam de dubluri
# x = {1, 2, '6', '7', '7'}  #nu e indexabil
# if 2 in x:  #cautare in set si lista
#     print("este")

# #dictionar
# a = {2: "35", 1: "3456"}
# print(a[1])
# a[1] = '222'  #se poate reatribui elementul, dar nu si cheia
# print(a)
# for x in a:
#     print(x)  #afiseaza doar cheile, care sunt unice
# for x in a:
#     print(f"{x} => {a[x]}")  #afiseaza si cheia si valoarea
# a1 = {1: 4}
# a.update(a1)  #adaugare element in dictionar
# a.update(y=3, b='a')  #adaugare element in dictionar
