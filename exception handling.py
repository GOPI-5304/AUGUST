# exception handling in python 

'''exception handing : in simple terms "the unwanted events or unexpected events disturb the normal flow of code 
or program at the time of execution"
in any programming languages the most common errors raised 

1. syntatical error or syntax error : its nothing but error raised due to when we write the code and we miss the 
we miss the proper syntax or wrong spelling is called syntax error
for example : 

a=10
b=20
print(a/b

its syntax error because we forgot the closed paranthesis while we print the code.

2.Run time errors : run time errors shoold be handled easy and programmer easily identified and rectified easily
while typing code 
*in simple terms the run time error is called exception 
* run time errors will give abnormal termination of program while execution.

handling exceptions : the exceptions should be handled by using try and except block.
for optional we execute finally and else exceptions. 
'''
# in python the built-in-exceptions are :

# 1.ZeroDivisionError: the zero division error occurs when we divide a number by 0(zero).
# for example :

n1=10
n2=0
if n1!=n2:
    print(n1/n2)
else:
    print("can not devided by zero")

# # to fix this zero division error by using try and except 

try:
    print(n1/n2)
except ZeroDivisionError as e:
    print("Error : Cant divide by zero ")


#  type error : type error should be raised whenever operation is performed on an incorrect object type 
# in simple terms when we perform operation between string and integer then raised type error

# for example : 

a=10
b="ten"
print(a+b)

# # to fix this exception by using try and except 

try:
    print(a+b)
except TypeError as e:
    print("Error : must be integers not string ")

# EOF Error : (END OF LINE Error)
# this arror is raised when input has reached the end of user input without receiving input
# for example :

n = int(input()) 
print(n * 10)


#  we can use multiple exceptions as different exceptions raised 

num1=10
num2=0
num3="ten"

try:
    print(num1-num3)
except ZeroDivisionError as e:
    print("error=the number cant be devided by 0 ")
except TypeError as e:
    print("error : must be integers not strings")
