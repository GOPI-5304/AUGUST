# inhritence task.
#  inheritence is nothing but inherits the values methods and objects from parents class
# and it executed by caling the object 

# types of inheritence : 

# single line inheritence :   it involves one parent and only one child inheritence 

#  for example : 

class user: # this a parent class
    def details(self):
        print("this is a parent class")
class view(user): # this is a child class 
    def view_details(self):
        print("this is child class")

# this is executed block by using object and 
s=view()
s.details()
s.view_details()

# in this only we take single parent class and one child class and it is called single inheritence method 


# multiple inheritence : in involves more than one parent class 


# we take two or more parent class and executed with help of single child class 

class father: # one parent class 
    def parent(self): # we use only instance method and instance variable 
        self.name="tharaka ramarao"
        print(self.name)

class mother: # second parent class 
    def parent_mother(self): # we use only instance method and instance variable
        self.name="kajal agarwal"
        print(self.name)

class child(father,mother): # this is a child class for execution of two parent classes 
    def child_details(self): # we use only instance method and instance variable
        self.child_name="harsha vardhan"
        print(self.child_name)

# execute the block of code by using object 
o=child()
o.parent_mother() # calling methods to execute 
o.parent() # calling methods to execute
o.child_details() # calling methods to execute 


# multilevel inheritence : in this level the child class acts as a parent class for another child class 
# that is one parent class can transfer methods and properties to child class and the chlild class acts as a parent class to another parent class 

# for example : 

# we take one parent class : 

class father: # one parent class 
    def parent(self): # we use only instance method and instance variable 
        self.name="tharaka ramarao"
        print(self.name)

class mother(father): # child class 
    def parent_mother(self): # we use only instance method and instance variable
        self.name="kajal agarwal"
        print(self.name)

class child(mother): # this is a child class for execution of two parent classes 
    def child_details(self): # we use only instance method and instance variable
        self.child_name="harsha vardhan"
        print(self.child_name)

# execute the block of code by using object 
o=child()
o.parent_mother() # calling methods to execute 
o.parent() # calling methods to execute
o.child_details() # calling methods to execute 

# hierachial inheritence : When more than one derived class are created from a single base this type of inheritance 
# is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# Example : 

class parent:
    def parent_details(self):
        self.name="nara chandrababu naidu"
        self.profession="chief minister of andhra pradesh"
        print("name :",self.name)
        print("profession :",self.profession)
class child1(parent):
    def child1_details(self):
        self.name="nara lokesh"
        print(self.name)
class child2(parent):
    def child2_details(self):
        self.name="nara devansh"
        print(self.name)
o1=child1()
o2=child2()
o1.parent_details()
o1.child1_details()
o2.child2_details()