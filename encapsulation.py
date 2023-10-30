

# encapsulation : Encapsultion is one of the important fundamental concept in object oriented programing and it defined as 
# it describes the idea of the wrapping data and methods that work on data with one unit. and it can prevent the 
# accidental modification of data

# For example : 

class Employee:
    def __init__(self, name, salary, project,company): # constructor 
        self.name = name # data members or attributes of class
        self.salary = salary # data members or attributes of class
        self.project = project # data members or attributes of class
        self.company=company
    # method 1 : 
    def show(self): # By using method we can display the attributes of class employee.
        print("Name: ", self.name) # accessing only personal details by using one method
    # method 2 : 
    def sal(self):
        print(f"The salary of {self.name} is {self.salary}")
    # method 3 :
    def work(self): # accessing professional details by using another method 
        print(f"employee in {self.company} working on the project of", self.project) # this is one of data member or attributes of class 
# NOTE : Both methods should and class should be bind getting into a single unit and run as single output.

# creating object of a class
emp = Employee('Gopi prince', 20000 , "Hospitality based system","Marolix software technologies")

# calling public method of the class
emp.show()
emp.sal()
emp.work()