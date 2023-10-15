
# calculator by oops concept 

class calculator:
    def __init__(self):
        self.number1=int(input("enter a number : "))
        self.number2=int(input("enter a number : "))
    def add(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1+self.number2)
    def substraction(self):
        print("The substraction of ",self.number1,"and",self.number2,"is : ",self.number1-self.number2)
    def multiplication(self):
        print("The multiplication of ",self.number1,"and",self.number2,"is : ",self.number1*self.number2)
    def division(self):
        print("The division of ",self.number1,"and",self.number2,"is : ",self.number1/self.number2)

while True:

    user=input("enter which function you want : ")
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
    next_function=input("enter yes or no for further step : ")
    if next_function=="yes":
        continue
    elif next_function=="no":
        break
    else:
        print("invalid input")
 