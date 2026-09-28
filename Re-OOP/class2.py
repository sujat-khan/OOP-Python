# Topic - Collection of objects

class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am ",self.name,"I am",self.age,"years old")

c1 = Customer("Nitish", 34)
c2 = Customer("Ankit", 45)
c3 = Customer("Neha", 32)

L = [c1, c2, c3]

# for i in L:
#     print(i.name, i.age)

for i in L:
    i.intro()