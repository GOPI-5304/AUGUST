#list assignments


# program on merge two lists 

print("1. program to merge a two lists")
list_a=list(eval(input("enter a list_a values : ")))
list_b=list(eval(input("enter a list_b values : ")))
merged_list=list_a+list_b

print(merged_list)


# program to find sum of list elemnts

print("2. python program to find sum of list elements")
list_a=list(eval(input("enter a list_a values : ")))
sum=0
for numbers in list_a:
    sum=sum+numbers
print(sum)



# python program on to find odd or even number 

print("3.python program on to find odd numbers or even numbers ")
list_a=list(eval(input("enter a numbers : ")))
even_list=[]
odd_list=[]
for numbers in list_a:
    if numbers%2==0:
        even_list.append(numbers)
    elif numbers%2!=0:
        odd_list.append(numbers)
print("even numbers : ",even_list)
print("odd numbers : ",odd_list)


# pyton program to delete given indexing element on the list

print("4.python program to delete the given indexing element in a list ")
list_a=["gopi","sai","samsng","vivo","oppo","kia cars"]
list_b=int(input("enter a particular indexing number : "))
list_a.pop(list_b)
print(list_a)


# pyton program to delete given indexing element on the list

print("5.python program to delete the given element in a list ")
list_a=list(eval(input("enter elements by seperating comma(,): ")))
list_b=int(input("enter a removing number : "))
list_a.remove(list_b)
print(list_a)

# pyton program to insert a element at the given indexing 

print("6.python program to add the given element at index position in a list ")
list_a=list(eval(input("enter a comma seperated numbers : ")))
list_b=int(input("enter elements by seperating comma(,): "))
list_c=int(input("enter a removing number : "))
list_a.insert(list_c,list_b)
print(list_a)


# pyton program to check the given two lists are same

print("7.python program to check the given two lists are same")
list_a=list(eval(input("enter a comma seperated numbers : ")))
list_b=list(eval(input("enter a comma seperated numbers : ")))
if list_a==list_b:
    print("The two given lists are same size")
else:
    print("The given two lists are different in size")



# 8.Python function that takes two lists and returns True if they have at least one common member

print("8.python function that takes two lists and returns if they have atleast one common number")

def list_a():
    list_1=list(eval(input("enter a comma seperated elements : ")))
    list_2=list(eval(input("enter a comma seperated elements : ")))
    for same_value in list_1:
        if same_value in list_2:
            return(True)
            break
    else:
        return(False)
print(list_a())


# 9.Python program to remove a specified column from a given nested list.

print("9.Python program to remove a specified column from a given nested list.")

list_a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list_b=[]
length=len(list_a)
for values in range(length):
    specified_value=list_a[values]
    specified_value.pop(1)
    list_b.append(specified_value)
print(list_b)


# 10.Python program to convert a list of multiple integers into a single integer.

print("10.python program to convert a list of multiple integers into single integer")
list_a=list(eval(input()))
for each_value in list_a:
    print(each_value,end="")


# Python program to convert a list of multiple integers into a single integer.

print("11.python program to remove duplicates from a list")

list_a=list(eval(input()))
list_b=set(list_a)
print(list_b)