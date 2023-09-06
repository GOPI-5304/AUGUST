# python script to add a key to dictionary

print("1.python script to add a key to dictionary")
dict={
    0:10,
    2:30
    }
dict[1]=20
print(dict)


# Python script to check weather a given key already exists in dictionaries

print("Python script to check weather a given key already exists in dictionaries")

dict_a={
    "name":"jai balayya",
    "age":62,
    "occupation":"indian actor"
}
if "name" in dict_a:
    print("True")
else:
    print("False")

# member ship method 

dict_a={
    "name":"jai balayya",
    "age":62,
    "occupation":"indian actor"
}

print("name" in dict_a)



# to iterate over dictionaries using for loops.

print("3.To iterate over dictionaries using for loops")

dictionary={
    "name":"jai balayya",
    "age":62,
    "occupation":"indian actor",
    "father_name":"Tharaka ramarao"
}

for keys in dictionary.items():
    print(keys)


# to print a dictionary where the keys are numbers between 1 and 15

print("4.To print a dictionary where the keys are numbers between 1 and 15")

num=dict()
for values in range(1,16): 
    num[values]=values**2
print(num)

#5.To create a dictionary from string

print("To create a dictionary from a string")
my_string="name age gender occupation charcter"
splitting=my_string.split()
dict={}

for name in splitting:
    dict[name]=dict.get(name,0)+1
print(dict)

# Python program to sum all the items in a dictionary.
print("6.Python program to sum all the items in a dictionary.")
dict_a={
    "a":100,
    "b":200,
    "c":300
}
print(sum(dict_a.values()))


#Python program to combine two dictionary by adding values for common keys.

print("7.Python program to combine two dictionary by adding values for common keys.")
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=dict(d1)
d3.update(d2)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)


#Python program to access dictionary key's element by index.

print("8.Python program to access dictionary key's element by index.")
dictionary={
    "physics":100,
    "chemistry":85,
    "maths":95
}
print(list(dictionary)[0])
print(list(dictionary)[1])
print(list(dictionary)[2])


# 9.Python program to remove a key from a dictionary

print("9.Python program to remove a key from a dictionary")
dictionary={
    "physics":100,
    "chemistry":85,
    "maths":95
}
del dictionary["physics"]
print(dictionary)

# python program to merge two python dictionaries.

print("10. python program to merge two python dictionaries")
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=(d1|d2)
print(d3)