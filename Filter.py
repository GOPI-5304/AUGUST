# Filter function : filter () is a built in function that allows you to process and extract the items from sequence of result.
# this function should return "True or False"
# syntax for filter function is : filter(function,sequence)

# programs on filter function.

# example : 1 
# Filter a vowels from given letters

letters=['a','b','c','d','e','i','o','u']

def get_vowels(letters):
    vowels=['a','e','i','o','u']

    if letters in vowels:
        return True
    else:
        return False
value=filter(get_vowels,letters)
print("The vowels are : ")
for each_item in value:
    print(each_item,end=",")



# Example : 2

# for getting non-vowels in above program

letters=['a','b','c','d','e','i','o','u']
def get_vowels(letters):
    vowels=['a','e','i','o','u']
    if letters in vowels:
        return False
    else:
        return True
value=filter(get_vowels,letters)
print("The non-vowels are : ")
for each_item in value:
    print(each_item,end=",")


# Example : 3

# python program to get the positive integers from list

def positive_integers(n):
    if n>=0:
        return True
    else:
        return False
list_a=(1,2,3,5,-9,-6,-5,-7,8,9,4,10,12,52,6,885)
value=filter(positive_integers,list_a)
print(list(value))


