############################# Inheriting Constructor #############
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# class FeaturePhone(Phone):
#     pass

# class SmartPhone(Phone):
#     pass

# s = SmartPhone(20000, "Apple", 13)

############################# Eg2 - Inheriting Private members #############
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# class FeaturePhone(Phone):
#     pass

# class SmartPhone(Phone):
#     def check(self):
#         print(self.__price)

# s = SmartPhone(20000, "Apple", 13)
# print(s.__price)

# concept- Child class cannot acccess hidden members of parent class

############################# Eg 3 - Polymorphism #############
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# class FeaturePhone(Phone):
#     pass

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a smartphone")

# s = SmartPhone(20000, "Apple", 13)
# s.buy()
# buy is presnt in parent and child, but s.buy() runs only child class method

# Example-1
# class Parent:

#     def __init__(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def show(self):
#         print("This is in child class")

# son = Child(100)
# print(son.get_num())
# son.show()

#Example-2
# class Parent:

#     def __init__(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self, val, num):
#         self.__val = val

#     def get_val(self):
#         return self.__val

# son = Child(100, 10)
# print("Parent: Num:", son.get_num())
# print("Child: Val:", son.get_val())

# Example-3
# class A:

#     def __init__(self):
#         self.var1 = 100

#     def display1(self, var1):
#         print("class A :", self.var1)

# class B(A):

#     def display2(self, var1):
#         print("class B :", self.var1)

# obj = B()
# obj.display1(200)

#Example-4
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# class FeaturePhone(Phone):
#     pass

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a smartphone")
#         super().buy()

# s = SmartPhone(20000, "Apple", 13)

# s.buy()

#Example-5

# class Phone:

#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):

#     def __init__(self, price, brand, camera, os, ram):
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print("Inside smartphone constructor")

# s = SmartPhone(20000, "Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)

# Example -6

# class Parent:

#     def __init__(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self, num, val):
#         super().__init__(num)
#         self.__val = val

#     def get_val(self):
#         return self.__val

# son = Child(100, 200)
# print(son.get_num())
# print(son.get_val())

# Example -7

# class Parent:
#     def __init__(self):
#         self.__num = 100

#     def show(self):
#         print("Parent:", self.__num)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var = 10

#     def show(self):
#         print("Child:", self.__var)

# dad = Parent()
# dad.show()
# son = Child()
# son.show()

#=================================================
#multi-level inheritance

# class Product:
#     def review(self):
#         print("Product customer review")

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s = SmartPhone(20000, "Apple", 12)
# p = Phone(1000, "Samsung", 1)

# s.buy()
# s.review()

#===================

############################# Multiple Inheritance #############

# # Parent Class 1
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a phone")

#     def return_phone(self):
#         print("Returning a phone")

# # Parent Class 2
# class Product:
#     def review(self):
#         print("Customer review")

# # Child Class inheriting from BOTH Phone and Product (Multiple Inheritance)
# class SmartPhone(Phone, Product):
#     pass

# # 1. Constructor call:
# # Python follows MRO (Method Resolution Order: SmartPhone -> Phone -> Product -> object)
# # Since SmartPhone has no __init__, Python executes Phone.__init__() first.
# s = SmartPhone(20000, "Apple", 12)

# # 2. Method call from Parent Class 1 (Phone)
# s.buy()

# # 3. Method call from Parent Class 2 (Product)
# s.review()


#========================

# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     # buy() method in Phone
#     def buy(self):
#         print("Buying a phone")

# class Product:

#     # buy() method with the exact same name in Product
#     def buy(self):
#         print("Product buy method")

# # Both parent classes have a buy() method.
# # In Python, the search order goes left to right: Phone is searched before Product.
# class SmartPhone(Phone, Product):
#     pass

# s = SmartPhone(20000, "Apple", 12)

# # Which buy() runs?
# # Because Phone is listed first in (Phone, Product), Phone.buy() is executed!
# s.buy()

# # MRO (Method Resolution Order)
# # You can inspect the search path at runtime using SmartPhone.mro() or SmartPhone.__mro__:
# # Order: [SmartPhone -> Phone -> Product -> object]
# print(SmartPhone.mro())

#=======================================================================================================
class A:

    def m1(self):
        return 20

# Class B inherits from A (Single inheritance)
class B(A):

    # B overrides m1() from A
    def m1(self):
        return 30

    def m2(self):
        return 40

# Class C inherits from B (Multi-level inheritance: A -> B -> C)
class C(B):

    # C overrides m2() from B
    def m2(self):
        return 20

obj1 = A()
obj2 = B()
obj3 = C()

# Step-by-step breakdown:
# 1. obj1.m1() -> Calls A.m1()               ==> 20
# 2. obj3.m1() -> Not in C, found in B.m1()   ==> 30
# 3. obj3.m2() -> Overridden in C.m2()        ==> 20
# Total: 20 + 30 + 20 = 70
print(obj1.m1() + obj3.m1() + obj3.m2())

#====================================================================