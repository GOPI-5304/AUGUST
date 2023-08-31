
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