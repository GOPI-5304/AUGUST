
# polymorphism is defined as the multiple classes declared with same methods 

# lets look into the examples :  
# polymorphic example on operators:
# example 1 :

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# example 2 :

num1 = 1
num2 = 2
print(num1+num2)

# polymorphic examples on functions 
# example : in python programming we use len function in every where 

print(len("programming"))
print(len("marolix"))

# Example 3: Polymorphism in Class Methods
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# method overiding : it is nothing but 
"""The child classes in Python also inherit methods and attributes from the parent class. "
We can redefine certain methods and attributes specifically to fit the child class, 
which is known as Method Overriding."""

# method overriding 
# example : Defining parent class 
class Parent():    
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"     # this constructor section have self.value attribute 
    # Parent's show method 
    def show(self): 
        print(self.value)       
# Defining child class 
class Child(Parent): 
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"  # this section also have the self.value attribute which is presdnt in parent class 
    # Child's show method 
    def show(self): 
        print(self.value) 
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

#  soo here the main concept is, the same attributes present in super and sub classes which is same in both is a method overiding.
obj1.show() 
obj2.show()



#  Method overloading : Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 
#    These methods are called overloaded methods and this is called method overloading.

#  example : 
# First product method.
# Takes two argument and print their product
def product(a, b):
    p = a * b
    print(p)
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)
# Uncommenting the below line shows an error
# product(4, 5) 
# This line will call the second product method
product(4, 5, 5)