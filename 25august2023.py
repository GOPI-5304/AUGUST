# to remove charcter from a string

string=input("enter a string : ")
string1=string.replace("g"," ")
print(string1)

print()
print() 

# python program to remove a charcter from string by using transalate method:

string=("marolix technologies is in hyderabad")
string_removed=input("enter a removed chartcer : ")
value=(string.translate({ord(string_removed):None}))
print(value)


 #program to check the string is palindrone or not 


string_value=input("enter a word : ")
last_value=""
for char in string_value:
    last_value=char+last_value
    if last_value==string_value:
        print("true")
    else:
        ("false")
print()
print()

# program to check the string is palindrone or not 

s=list(input("enter name: "))
value=s[::-1]
print(s==value)

# approach 3

s=input("enter name : ")
l=""
for char in s:
    l=char+l
print(l==s)

# approach 4

string=input("enter word : ")
rev=reversed(string)
if ("".join(rev))==string:
    print("True")
else:
    print("False")


#python program to check vowel or not
vowel=("a","e","i","o","u","A","E","I","O","U")

for char in vowel:
    charcter=input("enter a charcter: ")
    if char==charcter:
        print(charcter,"is a vowel")
    else:
        print(charcter,"is a consonants")

print()
print()

# write a python program to check no of vowels and consonents in given name 

name=input("enter string: ")
count=0
consonents=0
for i in name:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count=count+1
    elif (i!="a" or i!="e" or i!="i" or i!="o" or i!="u"):
        consonents=consonents+1
print("the nof vowels present in name is :",count)
print("the no of consonents in name is :",consonents)


# replace the string with another charcter

sub_string="check the given charcter is word or consonent"
string=input()
replace_method=sub_string.replace("word",string)
print(replace_method)

name=input("enter string: ")
ch="-"
result=name.replace(' ',ch)
print(result)


print()
print()


# count the alphabets, numbers and special charcters in the string

string=input("enter a string : ")

alphabets=0
digits=0
special_chars=0

for i in string:
    if i.isalpha():
        alphabets=alphabets+1
    elif i.isdigit():
        digits=digits+1
    else:
        special_chars+=1

print("alphabets: ",alphabets,"digits : ",digits, "special_chars : ",special_chars)

# python program to count the no of words repeated in the string 
string=input("enter name : ")
for name in string:
    value=string.count(name)
    print("the count of given string are : ",name,":",value)

print()
print()

#remove all the blank spaces from the string 
# 1
string=input()
sub_string=string.replace(" ","")
print(sub_string)

# 2
string=("marlolix software technologies").split()
print("".join(string)) 

# 3.By using translate method

string=("marlolix software technologies")
value=(string.translate({ord(" "):False}))
print(value)

print()
print()


#to find the sum of integers present in the string

strings=input()
sum=0
for i in strings:
    if i.isdigit():
        sum=sum+int(i)
print("sum=",sum)


# write a python program to find the some of integers from a string

string=input("enter a string :")
sum=0
for value in string:
    if value.isdigit()==True:
        result=int(value)
        sum=sum+result
print("The sum of digits in a string is :",sum)


print()
print()

# to remove the repeated charcyter from the string

string=input()
string1=string.replace("g","")
print(string1)


# by using conditional and loop concept for removing a repeated element from string

string=input("Enter a string : ")
new_list=[]
for char in string:
    if char not in new_list:
        new_list.append(char)
print(new_list)
for i in range(0,len(new_list)):
    print(new_list[i],end="")

print()
print()


# to write a program on the number of occurences present in a string

string=input("enter a string : ")
for alphabets in string:
    print(alphabets,"=",string.count(alphabets),"times")

# write a python program to count occurence of given charcter in a string 
# by using for loop concept count the occurences of a string

string=("write a python program to count occurence of given charcter in a string by using count method.")
counted_string=input("enter a counted string : ")
count=0
for i in string:
    if i==counted_string:
        count=count+1
print(count)


# write a python program to given strings are anagram or not

string1=input("enter name : ")
string2=input("enter string : ")

if sorted(string1)==sorted(string2):
    print("the words of ",string1,"and",string2,"are anagrams")
else:
    print(string1,"and",string2," are not anagrams")
