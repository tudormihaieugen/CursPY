# print("Primul meu string pentru \"curs 1\" " * 2)

# print(2+2*2-2/1)

# a = 'String'
# a += 'String1'
# print(type(a))

# concatenare cu format
# a = "String1"
# b = "String2"
# c = "{1} {0} {1}".format(a, b) #afiseaza string2 string1 string2
# c = a + ' ' + b #metoda clasica
# c = f"{a} {b}" #metoda noua
# print(c)

# a = 1
# b = 2
# c = int(a + b)
# print(c) #afiseaza 3

# a = "1"
# b = 2
# c = a + b
# print(c) #eroare string + int

# a = input("Nr1: ")
# b = input("Nr2: ")
# c = a + b
# print(c) #concatenare

# a = int(input("Nr1: "))
# b = int(input("Nr2: "))
# c = a + b
# print(c) #adunare int

# if conditie:
#     executie1
# elif conditie:
#     executie2
# else:
#     executie3

# a = True
# print(type(a))
# if a:
#   print("a este adevarat")

# a = 2
# b = a
# a = 3
# print(a)
# print(b)
# if a is b:
#     print("a este egal cu b")
# elif a > b:
#     print("a este mai mare")
# else:
#     print("a este mai mic")

# while conditie:
#     sintaxa1
#     ...
#     sintaxa2

# x = 10
# while x > 1:
#     print("x este ", x)
#     pass
#     x -= 1

# while True: #varianta cu int
#     euro = input("Valoare euro pentru convertire: ")
#     if euro.isdigit():
#         euro=int(euro)
#         print("Valoare convertita este:", euro * 4.87, "RON")
#     else:
#         print("Valoarea nu este un numar intreg")

# while True: #varianta cu int, float si string
#     euro = input("Valoare euro pentru convertire: ")
#     if euro.isdigit():
#         euro = int(euro)
#     elif "." in euro:
#         a = euro.split('.')
#         if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
#             euro = float(euro)
#     else:
#         print("Valoarea nu este un numar")
#         continue
#
#     print("Valoare convertita este:", euro * 4.87, "RON")

# while True: #varianta cu semn si meniu
#     print("1. Faceti conversie")
#     print("2. Iesiti din program")
#     ok = input()
#
#     if ok.isdigit() and int(ok) == 1:
#         euro = input("Valoare euro pentru convertire: ")
#         if len(euro) == 0:
#             continue
#         floatSign = 1
#
#         if euro[0] == "-":
#             floatSign = -1
#             euro = euro[1:]
#         if euro.isdigit():
#             euro = int(euro)
#         elif "." in euro:
#             a = euro.split('.')
#             if len(a) == 2 and a[0].isdigit() and a[1].isdigit():
#                 euro = float(euro)
#         else:
#             print("Valoarea nu este un numar")
#             continue
#
#         print("Valoare convertita este:", floatSign * euro * 4.87, "RON")
#     else:
#         break

# str = "abecedar"
# print(str[-1]) #ultimul caracter
# print(str[::-1]) #inverseaza string
#
# for poz, char in enumarete(str)
#     print(poz, char)
#
# for x in range(-1, 6, 2):
#     print(x)