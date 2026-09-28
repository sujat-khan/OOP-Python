class Customer:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(Customer):
    print(id(Customer))
    Customer.name='Tina'
    print(id(Customer))
    if Customer.gender=="Male":
        print("Hello MR",Customer.name)
    else:
        print("Hello Ms",Customer.name)

cust= Customer("Sujat","Male")
greet(cust)
print(id(cust))
print(cust.name)