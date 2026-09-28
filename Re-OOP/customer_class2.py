class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit_profile(self, new_name=None, new_city=None, new_pin=None, new_state=None):
        if new_name is not None:
            self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state

a=Address("kolkata",700016,"West Bengal")
cust=Customer('sujat','male',a)

cust.edit_profile("sujat","Gwalior",474001,"M.P")

print(cust.address.pincode)