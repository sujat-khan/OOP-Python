class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User):

    def entroll(self):
        print("Entroll")

    def review(self):
        print("Review")

# Student can access User class attributes but User cannot access Student class attributes
stu1 = Student()

stu1.login()
stu1.register()
stu1.entroll()
stu1.review()
    