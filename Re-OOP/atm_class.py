class Atm:

    #init is a consutructor
    # magic methods in python

    #class/class variable
    __counter=1

    def __init__(self):
        #instance variable

        self.__pin= ""
        self.__balance=0
        self.sno=Atm.__counter
        Atm.__counter+=1

        #self.__menu()
        # print("Hello from ATM")
        # print(id(self))
    
    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(val):
        if type(val)==int:
            Atm.__counter=val
        else:
            print("NOT Allowed")

    def get_pin(self):
        return self.__pin
    
    def get_balance(self):
        return self.__balance

    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin changed successfully")         
        else:
            print("NOT Allowed")

    def __menu(self):
        user_input = input("""
                    Hello, how would you like to proceeed?
                    1. Enter one to create pin
                    2. Enter two to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4. to check balance
                    5. Enter 5 to exit
            """
        )
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin=input("Enter your pin")
        print("Pin Set Successfully")

    def deposit(self):
        temp=input("Enter your pin")
        if temp== self.__pin:
            amount=int(input("Enter your amount"))
            self.__balance = self.__balance+ amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp=input("Enter your pin")
        if temp== self.__pin:
            amount=int(input("Enter your amount"))
            if amount< self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawl successful")
            else:
                print("insuficient funds")
        else:
            print("invalid pin")
    
    def check_balance(self):
        temp=input("Enter your pin")
        if temp== self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")

