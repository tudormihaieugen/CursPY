"""Clase"""

# class Masina:
#     pass
#
# Dacia = Masina()  # obiect


# stack = []
#
# def push(val):
#     stack.append(val)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(stack)
# print(pop())
# print(pop())
# print(pop())


# class Stack:
#     def __init__(self):  # definire constructor
#         self.stackList = []  # dublu underline = private
# 
#     def push(self, val):
#         self.stackList.append(val)
# 
#     def pop(self):
#         val = self.stackList[-1]
#         del self.stackList[-1]
#         return val
# 
# stackObject = Stack() 
# 
# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)
# 
# print(stackObject.pop())
# print(stackObject.pop())
# print(stackObject.pop())


# class Stack:
#     def __init__(self):  # definire constructor
#         self.__stackList = []  # dublu underline = private
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val

# stackObject1 = Stack()  # instantierea obiectului
# stackObject2 = Stack()
# stackObject3 = Stack()
#
# stackObject1.push(1)
# stackObject2.push(stackObject1.pop() + 1)
# stackObject3.push(stackObject2.pop() - 2)
#
# print(stackObject3.pop())


# class Stack:
#     def __init__(self):  # definire constructor
#         self.__stackList = []  # dublu underline = private
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# class AddingStack(Stack):  # mostenire de clasa
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def getSum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
# stackObject = AddingStack()
#
# for i in range(5):
#     stackObject.push(i)
# print(stackObject.getSum())  # sum = 10
#
# for i in range(5):
#     print(stackObject.pop())  # 10 4 3 2 1 0


# class ExampleClass:
#     def __init__(self, val=1):
#         self.first = val
#
#     def setSecond(self, val):
#         self.second = val
#
# obj1 = ExampleClass()
#
# obj2 = ExampleClass(2)
# obj2.setSecond(3)
#
# obj3 = ExampleClass(4)
# obj3.third = 5
#
# print(obj1.__dict__)  # dict afiseaza toate proprietatile obiectului
# print(obj2.__dict__)
# print(obj3.__dict__)


# class ExampleClass:
#     def __init__(self, val=1):
#         self.__first = val
#
#     def setSecond(self, val):
#         self.__second = val
#
# obj1 = ExampleClass()
#
# obj2 = ExampleClass(2)
# obj2.setSecond(3)
#
# obj3 = ExampleClass(4)
# obj3.__third = 5
#
# print(obj1.__dict__)  # dict afiseaza inclusiv proprietatile private
# print(obj2.__dict__)
# print(obj3.__dict__)


# class Example:
#     counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         Example.counter += 1
#
# obj1 = Example()
# obj2 = Example(2)
# obj3 = Example(4)
# print(obj1.__dict__, obj1.counter)
# print(obj2.__dict__, obj2.counter)
# print(obj3.__dict__, obj3.counter)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         Example.__counter += 1
#
# obj1 = Example()
# obj2 = Example(2)
# obj3 = Example(4)
# print(obj1.__dict__, obj1._Example__counter)  # acceseaza variabila privata counter
# print(obj2.__dict__, obj2._Example__counter)
# print(obj3.__dict__, obj3._Example__counter)


# class Example:
#     variabila = 1
#
#     def __init__(self, val):
#         self.var2 = 3
#         Example.variabila = val
#
# print(Example.__dict__)  # afisarea tuturor proprietatilor clasei
# obj1 = Example(2)
#
# print(Example.__dict__)
# print(obj1.__dict__)


# class Example:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
# 
# obj1 = Example(1)
# print(obj1.a)
# print(obj1.b)  #eroare deoarece obj1 nu are atributul b


# class Example:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
# obj1 = Example(1)
# print(obj1.a)
#
# try:
#     print(obj1.b)
# except AttributeError:  # eroare specifica daca nu exista atributul
#     pass


# class Example:
#     attr = 1
#     __attr2 = 2
#
# print(hasattr(Example, 'attr'))  # metoda de cautare atribut -> returneaza True/False
# print(hasattr(Example, '__attr2'))  # daca variabila e privata, nu o gaseste
# print(hasattr(Example, 'prop3'))


# class Example:
#     def method(self):
#         print('method')
#
# obj = Example()
# obj.method()


# class Classy:
#     variabila = 2
#
#     def method(self):
#         print(self.variabila, self.var)
#
# obj = Classy()
# obj.var = 3  # var este definit in afara clasei, dar poate fi folosit
# obj.method()


# class Classy:
#     def other(self):
#         print("other")
#
#     def method(self):
#         print("method")
#         self.other()
#
# obj = Classy()
# obj.method()


# class Classy:
#     def __init__(self, value=None):
#         self.var = value
#
# obj1 = Classy("object")
# obj2 = Classy()
# print(obj1.var)
# print(obj2.var)


# class Classy:
#     def visible(self):
#         print("visible")
#
#     def __hidden(self):
#         print("hidden")
#
# obj = Classy()
# obj.visible()
#
# try:
#     obj.__hidden()
# except:
#     print('failed')
#
# obj._Classy__hidden()


# class Classy:
#     variabila = 1
#
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
# obj = Classy()
# print(obj.__dict__)
# print(Classy.__dict__)


# class Class:
#     pass
#
# print(Class.__name__)
# obj = Class()
# print(type(obj).__name__)  # Afisarea numelui clasei din care face parte


# class SuperOne:
#     pass
#
# class SuperTwo:
#     pass
#
# class SuperThree(SuperOne, SuperTwo):
#     pass
#
# class SuperFour(SuperThree):
#     pass
#
# def printBases(cls):
#     for x in cls.__bases__:
#         print(x.__name__)
#
# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(SuperThree)
# printBases(SuperFour)


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):  # str reprezinta rezultatul clasei
#         return f"{self.name} in {self.galaxy}
#
# sun = Star("Sun", "Milky Way")
# print(sun)


# class Vehicule:
#     pass
#
# class VehiculeDeTractare(Vehicule):
#     pass
#
# class VehiculeCuRemorca(VehiculeDeTractare):
#     pass
#
# for cls1 in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
#     for cls2 in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()
#
# obj1 = Vehicule()
# obj2 = VehiculeDeTractare()
# obj3 = VehiculeCuRemorca()
#
# for obj in [obj1, obj2, obj3]:
#     for cls in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
#         print(isinstance(obj, cls), end='\t')
#     print()


# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
# obj1 = SampleClass(0)
# obj2 = SampleClass(2)
# obj3 = obj1  # Face referire la aceeasi zona de memorie
# obj3.val += 1  # Adauga si la obj1 si la obj3 !!!
#
# print(obj1 is obj2)  # False
# print(obj2 is obj3)  # False
# print(obj3 is obj1)  # True
# print(obj1.val, obj2.val, obj3.val)  # 1 2 1
# str1 = "Maria are mere "
# str2 = "Maria are mere galbene"
# str1 += "galbene"
# print(str1 == str2, str1 is str2)  # True False


# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"mY name is {self.name}"
#
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#
# obj = Sub("Nume")
# print(obj)


# class Parinte:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"mY name is {self.name}"
#
#
# class Sub(Parinte):
#     def __init__(self, name):
#         super().__init__(self)  # face referire la clasa parinte
#
#
# obj = Sub("Nume")
# print(obj)


# class Super:
#     a = 1
#
# class Sub(Super):
#     b = 2
#     a = 2  # preia atributul din clasa copil
#
# obj = Sub()
# print(obj.b)
# print(obj.a)


# class Super:
#     def __init__(self):
#         self.supVar = 11
#
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
#
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


# class Level1:
#     varia1=100
#
#     def __init__(self):
#         self.var1 = 101
#
#     def fun1(self):
#         return 102
#
# class Level2(Level1):
#     varia2 = 200
#
#     def __init__(self):
#         super().__init__()
#         self.var2 = 201
#
#     def fun2(self):
#         return 202
#
#     def fun1(self):  # suprascrie metoda din Level1
#         return 444
#
# class Level3(Level2):
#     varia3 = 300
#
#     def __init__(self):
#         super().__init__()
#         self.var3 = 301
#
#     def fun3(self):
#         return 302
#
# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())


# class Left:
#     var = "L"
#     varLeft = "LL"
#     def fun(self):
#         return "Left"
#
# class Right:
#     var = "R"
#     varRight = "RR"
#     def fun(self):
#         return "Right"
#
# class Sub(Left, Right):
#     pass
#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())
