# interview coding quetions on string.py

# 1.python program to remove charcter from string 

string="marolix software technologies"
value=string.replace("a","")
print(value)

# 2.python program to count no of ocurences in a string
string=input("enter a string : ")
char=input("enter charcter : ")
count=0
for i in range(len(string)):
    if (string[i]==char):
        count=count+1
print(f"the count of {char} is ",count)

# 3.check the given strings are anagram or not 

string1=input("enter string : ")
string2=input("enter string : ")
print(sorted(string1))
print(sorted(string2))
if sorted(string1)==sorted(string2):
    print("the given strings are anagrams")
else:
    print("write the proper words")
    
# 4.python program to check the given word is palindrone or not 
# palindrone means the word reads same as when we read reverse
string=input("enter a string : ")
rev=string[::-1]
if rev==string:
    print("the given string is palindrone")
else:
    print("entered word is a not palindrone")

# 4a.python program to check the given word is palindrone or not
string=input("enter a string : ")

if string==string[::-1]:
    print("the given word is palindrone")
else:
    print("not a palindrone word")

# 5.python program to check the given charcter is vowel or consonent

v1=("aeiou")
chr=input("enter word : ")
if chr in v1:
    print("the word is vowel")
else:
    print("consonant")

# 6. check the given charcter is digit or not

num=input("enter charcter : ")
digit=0
for char in num:
    if char.isdigit():
        print("the given charcter is a digit ")
    else:
        print("the charcter is alphabet")

# 7. check the given charcter is digit or not by using isdigit method
num=input("enter charcter : ")
value=num.isdigit()
print(value)

# 8. replace the string space with given charcter
string="marolix software technoogies is a god company for better environment"
chr=input("enter chatcter : ")
result="" 
for i in string:
    if i==" ":
        i=chr
    result=result+i
print(result)

# 9. replace the string space with given charcter using replace method
string="marolix software technoogies is a god company for better environment"
chr=input("enter chatcter : ")
value=string.replace(" ",chr)
print(value)

# 10. write python program to convert lower case charter to upper case charcter
string="marolix software technologies"
value=string.upper()
print(value)

# 11. write python program to convert lower case vowel to upper case
value="marolix software technologies"
vowels="aeiou"
for i in value:
    if i in vowels:
        upper_case=i.upper()
        value=value.replace(i,upper_case)
print(value)

# 12.python program to delete vowels in string
#taking the input string from the user
string = input("Enter a String : ") 
result=''
vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for i in string:  
    if i in vowels: # searching for vowels in string
        i="" # replace sting with empty space
    result += i # concatenate after removing strings
print("String after removing the vowels :",result)

# python program print highest frequency of charcter in a string.
#taking the input string from the user
string = input("Enter a String : ") 
dict={}
for char in string:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1
frequency_values=max(dict.values())
for char in dict:
    if dict[char]==frequency_values:
        print(char,end=" ")
    
# python program to print replace the vowel with first occurence of vowel with "_" in a string
string=input("enter a string : ")
vowels=("a","e","i","o","u")
for i in range(len(string)):
    if string[i] in vowels:
        string=string[:i]+"-"+string[i+1:]
print(string)

# python program to print replace the vowel with first occurence of vowel with "_" in a string
string=input("enter string : ")
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        string=string.replace(char,"-")
print(string)
   
# python program to count alphabets digits and special charcters from string
string=input("enter string : ")
alphabets=0
digits=0
charcters=0
for i in string:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        digits+=1
    else:
        charcters+=1 
print(f"alphabets:{alphabets} digits :{digits} charcters:{charcters}")
        
# python program to seperate charcters from a string 
string=input("enter a string : ")
seperated="  ".join(string)
print(seperated)

# python program to remove blank space from a string 
string=input("enter a string : ")
blankSpace=string.replace(" ","")
print(blankSpace)

# python program to concatenate two strings by using join method
s1="gopi"
s2="prince"
join=" ".join([s1,s2])
print(join)

# python program to concatenate two strings 
s1="gopi"
s2="prince"
join=s1+" "+s2
print(join)

# python program to remopve a repeated charcter from string.
string="programming"
s=[]
for char in string:
    if char not in s:
        s.append(char)
    v="".join(s)
print(v)

# python program to calculate sum of integers present in a string
string=input("enter string :")
sum=0
for i in string:
    if i.isdigit():
        sum+=int(i)
print(sum)
    
# print all the words except occurences in string
string=input("enter a string :")
d={}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
value=max(d.values())
result=""
for i in d:
    if d[i]==1:
        result=result+i
print(result)

#Python program to copy one string to another string.
# by slicing method 
string=input("enter a string :")
# use slicing 
v=string[:]
print(string)
print(v)

# by using for loop method 
string= input("enter string : ")
s=""
for i in string:
    s=s+i
print(string)
print(s)

# python program to set the string in ascending order
string="gopiprince"
s=list(string)
asc="".join(sorted(s))
print(asc)

# python program to set the string in descending order
string="gopiprince"
s=list(string)
asc="".join(sorted(s,reverse=True))
print(asc)
