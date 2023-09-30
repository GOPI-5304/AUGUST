

# To create a simple calculator:

print("task : 5 :- to create a simple calculator by using python functions")

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

print("select the which operation you want : ")
print("add")
print("substraction")
print("multiplicatiion")
print("division")

while True:
    input_user=input("enter the which operation you want : ")
    first_number=int(input("enter the 1st number : "))
    second_number=int(input("enter the second number : "))

    if  input_user=="add":
        print(first_number,"+",second_number,"=",add(first_number,second_number))
    elif input_user=="substraction":
        print(first_number,"/8",second_number,"=",division(first_number,second_number))
    else:
        print("valid input")
    next_input=input("lets go to the next calculation : (yes/no) : ")
    if next_input=="yes":
        continue
    elif next_input=="no":
        break
    else:
        print("invalid input")

    
# Approach 2

num1=float(input("enter 1st number : "))
num2=float(input("enter 2nd number : "))
input_user=input("select which operation you want +,-,*,/ : ")

if input_user=="+":
    result=num1+num2
elif input_user=="-":
    result=num1-num2
elif input_user=="*":
    result=num1*num2
elif input_user=="/":
    result=num1/num2
else:
    print("invalid input")

print("The final result of two numbers is : ",result)

