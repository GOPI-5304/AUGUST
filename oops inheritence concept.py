# students count difference by no of boys and girls 

# inheritence method : inheritence method is nothing but declare the parent class by using child class
# i.e it inherites (received) methods and properties and also value of variebles from one class to another class 
# that is from parent class -----> child class "child class received methods and properties from parent class"

# types of inheritence method :

# 1.single inheritence method := only wii we execute one parent class and child class "i.e it allows only one child and parent class"

# 2.multiple inheritence method := it allows more than one parent class "i.e one or more parent class with one child class"

# 3.multilevel inheritence method := in this the child class acts as parent class for another child class.

# 4.hierachial inheritence method := it involves more than one inheritence method 



# Example : this is single inheritence method.
class student:
    def student_details(self):
        self.std=int(input("enter standard : "))
        print(self.std)
class boys(student):
    def strength_details(self):
        strength_boys=int(input("enter strength of boys: "))
        strength_girls=int(input("enter strength of girls: "))
        if strength_boys>strength_girls:
            print("the boys are highest with difference of ",strength_boys-strength_girls,"members")
        else:
            print("the girls are highest with difference of ",strength_girls-strength_boys,"members")

s=boys()
s.student_details()
s.strength_details()


# Example : this is multiple inheritence method : 
class boys:
    def boyes(self):
        print("the boys are present half of the full strength ")
class girls:
    def girl(self):
        print("girls also pressent half of the full strength")

class standard(boys,girls):
    pass

s=standard()
s.boyes()
s.girl()


# Example : this is multilevel inheritence method : 
