# #FUNCTII
# def primaFunctie():
#     #corpul functiei
#     pass


# def message():
#     print("Enter a value: ")
#
# message()


# def hello(name):
#     print("hello", name)
#
# name1 = input("Enter your name: ")
# hello(name1)


# def hello(name="MIHAI"):  #valoare default
#     print("hello", name)
#
# name1 = input("Enter your name: ")
# hello()


# def message(what, number):
#     print("Enter", what, "number", number)
#
# message('telephone', 11)


# def message(what, number='2'):  #default se pune intotdeauna la FINAL
#     print("Enter", what, "number", number)
#
# message('telephone')


# def message(what='phone', number='2'):
#     print("Enter", what, "number", number)
#
# message(number='3', what='number')  #Tasta P = vizualizare parametrii


# def message(what='phone', number='2'):  #ghilimele si doua puncte = documentatie automata
#     """
#     :param what:
#     :param number:
#     :return:
#     """
#     print("Enter", what, "number", number)
#
# message(number='3', what='number')  #Tasta P = vizualizare parametrii


# def suma(a, b, c):
#     print(f"{a} + {b} + {c} =", a + b + c)
#
# suma(3, c=1, b=2)


# def HappyNewYear(wishes=True):
#     print("3")
#     print("2")
#     print("1")
#     if not wishes:
#         return
#     print("Happy new year!")
#
# HappyNewYear()


# def name():
#     return 123
#
# a = name()
# print(a)


# def sumOfList(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
#
# a = sumOfList([5, 4, 3])
# print(a)  #print 12


# def sumOfList(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
#
# a = sumOfList([5, 4, 3])
# print(a)  #print 5 -> return iese din functie


# def litere(litera: str) -> bool:  #parametrul de intrare e recomandat sa fie str si parametrul de iesire e recomandat sa fie boolean
#     if isinstance(litera, str):
#         return True
#     else:
#         return False


# import calendar
#
# def an_bisect(an: int) -> bool:
#     if calendar.isleap(an):
#         return True
#     return False
#
# an = input("An: ")
# try:
#     an = int(an)
# except ValueError:
#     print("Nu ati introdus un numar")
#
# print("Anul este bisect" if an_bisect(an) else "Anul nu este bisect")


# import datetime
#
# def validareDATA(zi, luna, an) -> bool:
#     try:
#         a = datetime.datetime.strptime(f"{zi}.{luna}.{an}", "%d.%m.%Y")
#         return True
#     except:
#         return False
#
# a = validareDATA(23, 7, 2000)
# print(a)
# b = validareDATA(23, 17, 2000)
# print(b)


# import datetime
#
# def validareDATA(zi, luna, an) -> bool:
#     try:
#         a = datetime.datetime.strptime(f"{zi}.{luna}.{an}", "%d.%m.%Y")
#         print(a)
#         # return True
#     except Exception as e:  #doar atunci cand exista exceptii
#         # return False
#         print(e)
#     else:
#         print("Else")
#     finally:  #se executa MEREU si apoi iese din try/except
#         print("Data este:", zi, luna, an)
#
# a = validareDATA(23, 7, 2000)
# print(a)


# import math
#
# def isPrime(numar: int) -> bool:
#     if numar < 2:
#         return False
#     elif numar == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(numar))):
#             return False
#     return True
#
# a = isPrime(2)
# print(a)


# def mutiply(a, b):
#     return a * b
#
# print(mutiply(3, 4))


# def wishes():
#     print("My wishes")
#     return "Happy"
#
# wishes()
# print(wishes())
# w = wishes()
# print(w)


# def Hi(MyLIST):
#     for name in MyLIST:
#         print(f"Hi, {name}")
#         return 'a'
#
# a = Hi(['Adam', 'John', 'Lucy'])
# print(a)


# def createList(n):
#     myList = []
#     for i in range(n):
#         myList.append(i)
#     return myList
#
# print(createList(5))


# def hi():
#     return
#     print("Hi")
#
# hi()


# def isInt(DATA):
#     if type(DATA) == int:
#         return True
#     elif type(DATA) == float:
#         return False
#
# print(isInt(5))
# print(isInt(5.0))
# print(isInt("5"))


# def evenNumLst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
#
# print(evenNumLst(11))


# def listUpdater(lst):
#     updList = []
#     for elem in lst:
#         elem **= 2  #la puterea a doua
#         updList.append(elem)
#     return updList
#
# l = [1, 2, 3, 4, 5]
# print(listUpdater(l))


# def scopeTest():
#     x = 123
#
# scopeTest()


# def myFunction():
#     var = 2
#     print('Var este: ', var)
#
# var = 1
# myFunction()
# print(var)


# def myFunction():
#     global var
#     var = 2
#     print('Var este: ', var)
#     return var
#
# var = 1
# myFunction()
# print(var)


# var = 3
# def myFunction():
#     var = 2
#     print('Var este: ', var)
#     return var
#
# myFunction()
# print(var)


# var = 2
# def multByVar(x):
#     return x * var
#
# print(multByVar(7))


# def multByVar(x):
#     var = 7
#     return x * var
#
# var = 3
# print(multByVar(7))
# print(var)


# var = 2
# print(var)
#
# def multByVar():
#     global var
#     var = 5
#     return var
#
# print(multByVar())
# print(var)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(4))


# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
#
# print(fun(25))


# def operatie(a, b):
#     return a + b, a * b
#
# x, y = operatie(2, 3)
# print(x, y)
