#ASSIGNMENTS
# 1.membership checking

#example:1 (in operator)

name="im a employee in marolix software solutions"
input_name=input()

if input_name in name:
    print(" YES : Word present in name ")
else:
    print("NO: word not present in name")

print("---------------------------------------------------------------")

#example:2

word="im software developer in marolix software solutions"
input_word=input()

result=input_word in word

print(result)

#example:3

names=["jr ntr","mahesh babu","pavan kalyan","ram charan"]
input_name=input()

for input_name in names:
    if input_name in names:
        print(input_name,"is present in names")
    else:
        print(input_name,"is not present in names")



# strip method 

#example:1

name="     gopi prince sai teja   "
name1=name.strip()
length=len(name1)
print(length)

#example:2

text = "     banana     "
x = text.strip()
print("out of all fruits", x, "is my favorite")

#example:3

text_word = ",,,,,ggggoooo.....banana....rrr"
x = text_word.strip(",.ggoo")
print(x)

#comparing two strings

#example:1

fruit=input()

if fruit=="apple":
    print("Yes it is apple")
elif fruit=="banana":
    print("yes its banana")
elif fruit=="orange":
    print("yes its orange")
elif fruit=="mango":
    print("yes its mango")
else:
    print("no fruit matched")

#example:2

string_x = 'Hello & Welcome'
string_y = 'Hello & Welcome'


if string_x == string_y:
 
    print ("Same Strings")
 
else:
 
    print ("Different Strings")

#example:3

n1=input()
n2=input()

if n1==n2:
    print("student profile matched")
else:
    print("student profile is not matched")


#index method

fruits = ['apple','banana','cherry','orange','gua','pineapple']
x = fruits.index("cherry")
print(x)

fruits = ['apple','banana','cherry','orange','gua','pineapple']
x = fruits.rindex("cherry")
print(x)

#rindex method

fruits = "apple is a healthy fruit"
x = fruits.rindex("fruit",0,24)
print(x)

# find method

fruits = "apple is a healthy fruit"
x = fruits.find("fruit")
print(x)


# rfind method

fruits = "apple is a healthy fruit"
x = fruits.rfind("fruit",15,24)
print(x)


#replacing the string

string1="marolix is a medical coding company in hyderabad"
string2=string1.replace("medical coding","software solution pvt ltd")
print(string2)

sentance="teh cat and teh dog"
sentance2=sentance.replace("teh","the")

print(sentance2)

#split method


sentance="cat buffellow horse zirafee dog"
sentance2=sentance.split()

print(sentance2)

#example:

cars="bmw,-tesla,-benz,-audi,-rolls royce"
print(cars.split())


# joining method 

variable="python is " , " powerful progr","mming l","nguage"
print("a".join(variable))