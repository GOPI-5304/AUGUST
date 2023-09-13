# Map function: map function is defined as the " map function should be applied each item in sequence"
# For example : if numbers from 1 to 10 in list and the map function is applied to 1,2,3,4,5,6,7,8,9,10 by adding or multiplication or else any mathematical operation

# Syntax : map(function,sequence)

# Example : 1

def sum_of_numbers(n):
    if n+n%2==0 or n+n%2!=0:
        return n+n
    else:
        return n
n=(1,2,3,4,5,6,7,8)
result=list(map(sum_of_numbers,n))
print(result)



# Example : 2

# Caculate length of each word in a tuple

def length(string):
    return len(string)
string=("samba","narasimhudu","andhrawala","brundavanam","kanthri")
result=map(length,string)
print(list(result))


# Example : 3 

# Python program on adding two numbers by using different argements by applying map function.

def adding_numbers(a,b):
    return a+b
string=map(adding_numbers,('1','2','3'),('4','5','6'))
print(list(string))