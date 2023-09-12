# lambda functions : lambda function is nothing bus single line function.for avoiding the multiple lines

# Example : 1
# python program to add the given number with 15 and multiplies with 15

x=int(input("Enter a first value : "))
y=int(input("Enter a second value"))
var=lambda x,y : x*y
print(var(x,y))


# example : 2
# write a python program to check the given number is positive or negative number

a=int(input("enter a number : "))
var=lambda a : "positive integer" if a%2==0 else "odd"
print(var(a))

# example : 3
# writw a python program to find a square number by given input number

a=int(input("Enter a number : "))
var=lambda a:  a*a
print("The square of given number is :",var(a)) 