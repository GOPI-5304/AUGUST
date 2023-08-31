
#adding elemets in the list by using append method

list_a=['gopi','sai','chandu']
list_b=("gopi prince")
list_a.append(list_b)
print(list_a)

print()
print()

#adding charcters to the empty list by using append method

empty_list=[]
empty_list.append("1,2,3,4,5,6,7,8,9,10")
print(empty_list)

print()
print()



#adding existing list by using append method

list_a=["tech mahindra,infosys,tcs,accenture"]
list_b=["marolix,kastech,corohealth"]
list_a.append(list_b)
print(list_a)

print()
print()

#index method 

list_a=["apple","orange","banana","pineaple"]
list_b=list_a.index("banana")
print(list_b)

print()
print()

color_list = ["Red", "Orange", "Yellow", "Pink", "Green", "Blue", "Purple", "Black", "White"]

list_a=int(input())
list_a=color_list[list_a]
print(list_a)

print()
print()


# extend method

list_a=[1,2,3,4,5,6]
list_b=[7,8,9,10,11,12,13,14,15,16,17,18,19]
list_a.extend(list_b)
print(list_a)

#extend method

list_a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_b=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
list_a.extend(list_b)
print(list_a)


# insert a existing element into list

list_a=[1,3,4,5,6,7,8]
list_a.insert(1,2)
print(list_a)


# insert a existing element into list

list_a=[1,3,4,[1,2,3,4],6,7,[8,9,10,11]]
list_a.insert(6,12)
print(list_a)


#pop method: this method is used to remove the last element in a list 

list_a=[1,2,3,4,5,6,6]
list_a.pop()
print(list_a) 


#pop method: this method is used to remove the last element in a list 

list_a=["sathwika","sasikala","manikanta babu","yshwanth","thulasi manikanta"]
list_a.pop()
print(list_a)


#pop method: this method is used to remove the last element in a list 

list_a=["mamatha miss","krishna kumari miss","swaroopa miss","bhagya bhai miss","anjali miss","rama devi miss"]
list_a.pop()
print(list_a) 


#finding elements by using member ship checking 
list_a=["fortuner","innova crysta","kia seltos","kia carnival","kia sonet","brezaa","shift vdi","shift dzire","alto 800"]
list_b=input()
list_c=list_b in list_a
print(list_c)


print()
print()

#finding the vehicles names by using member ship checking 

vehicles=["fortuner","innova crysta","kia seltos","kia carnival","kia sonet","brezaa","shift vdi","shift dzire","alto 800"]
checking_value=int(input())
for i in range(checking_value):
    input_value=input("checking vehicle : ")
    if input_value in vehicles:
        print("True")
    else:
        print("False")
        


# creating a list by using listy comprehension 

new_list="gopi"
list_comprehension=[name for name in new_list]
print(list_comprehension)



# creating list by using for loop 

new_list=[]
for i in range(1,10+1):
    new_list.append(i)
print(new_list)



#creating a list by using while loop 

new_list=[]
counter=0
while counter < 10:
    new_list.append(counter)
    counter=counter+1
print(new_list)


# creating list and take out the names of the word present "a"

vehicles=["fortuner","innova crysta","kia seltos","kia carnival","kia sonet","brezaa","shift vdi","shift dzire","alto 800"]
new_list=[]
for name in vehicles:  
    if "a" in name:
        new_list.append(name)  
print(new_list)



# To write a simple program to dispLay the words which vowels would be present.

vowels=["a","e","i","o","u"]
names=("fortuner is a best car forever and ever")
empty_list=[]
for name in names:
    if name in vowels:
        if name not in empty_list:
            empty_list.append(name)
print(empty_list)  
            

# to create a size of list

# Here
new_list=int(input())
empty_list=[]

for list_size in range(new_list):
    new_input=input("enter a string : ")
    empty_list.append(new_input)
print(empty_list)
