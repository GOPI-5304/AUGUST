# python programs on recursion.
# Recursion is defined as "A function calling it self " without loops we can easily write the code.

# example : 1

# sum of numbers in a given input
def sum_of_numbers(number):
    if number==1:
        return number
    else:
        return number * sum_of_numbers(number-1)

number=int(input("give a factorial number : "))
result=sum_of_numbers(number)
print("The factorial number of",number,"is : ",result)



# example : 2

# Sum of squares of numbers in a given list
def squares(num):
    each_num=int(num[0])
    if len(num)==1:
        return each_num**2
    else:
        return each_num**2 + squares(num[1:])
num=input("Enter a number : ").split()
print(squares(num))



# example : 3

# python program to print sum of numbers in a given string

def squares(num):
    if num==1:
        return num
    else:
        return num + squares(num-1)
num=input("Enter a number : "))
print(squares(num))
