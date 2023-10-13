
# calculator by oops concept 

class calculator:
    def __init__(self):
        self.number1=int(input("enter a number : "))
        self.number2=int(input("enter a number : "))
    def add(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1+self.number2)
    def substraction(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1-self.number2)
    def multiplication(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1*self.number2)
    def division(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1/self.number2)

user=input("enter which function you want : ")
print()
cal=calculator()
if user=="add":
   cal.add()
elif user=="substraction":
    cal.substraction()
elif user=="multiply":
    cal.multiplication()
elif user=="division":
    cal.division()
else:
    print(user,"function not existed in class")
print()