
# Math function : it is one of the built-in function that imports the mathemetical functions 
# import math or from math import *

# example : 1
# Python program to convert value in degreess to radian

from math import *

# The actual formula of degrees converted to radian is : "degrees * π/180"

pi=22/7
degree=float(input("enter a value : "))
radian=degree*(pi/180)
print(radian)
 
# The direct method to convert degrees to radians is : radians()

value=int(input("enter a value : "))
degree=radians(value)
print(degree)

print("-----------------------------------------------------------------------------------------------")


# Example : 2

# Write a python program to calculate the area of trapezoid.

a=float(input("Enter a value : "))
b=float(input("Enter b value : "))
height=float(input("Enter a height of the value : "))
trapezoid=fsum([a,b])
product_value=trapezoid/2*height
print("the area of trapezoid is : ",product_value)

print("-------------------------------------------------------------------------------------------------")

# Example : 3 

# python program to convert a negative number to positive number

n=float(input())
print("The negative number of ",n,"converted positive number of ",abs(n))

print("------------------------------------------------------------------------------------------------")
# Example : 4

# python program to power of value 

num_1=float(input("enter a powered value : "))
num_2=float(input("enter a value that power with : "))
value=pow(num_1,num_2)
print("The power of",ceil(num_1),"is",ceil(value))