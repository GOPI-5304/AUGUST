# to remove charcter from a string

string=input("enter a string : ")
string1=string.replace("g"," ")
print(string1)

print()
print() 


 #program to check the string is palindrone or not 


string_value=input()
last_value=""
for char in string_value:
    last_value=char+last_value
    if last_value==string_value:
        print("true")
    else:
        ("false")
print()
print()


vowel=("a","e","i","o","u","A","E","I","O","U")

for char in vowel:
    charcter=input("enter a charcter: ")
    if char==charcter:
        print(charcter,"is a vowel")
    else:
        print(charcter,"is a consonants")

print()
print()

# replace the string with another charcter

sub_string="check the given charcter is word or consonent"
string=input()
replace_method=sub_string.replace("word",string)
print(replace_method)

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

print()
print()

#remove all the blank spaces from the string 

string=input()
sub_string=string.replace(" ","")
print(sub_string)


print()
print()


#to find the sum of integers present in the string

strings=input()
sum=0
for i in strings:
    if i.isdigit():
        sum=sum+int(i)
print("sum=",sum)

print()
print()

# to remove the repeated charcyter from the string

string=input()
string1=string.replace("g","")
print(string1)

print()
print()


# to write a program on the number of occurences present in a string

string=input("enter a string : ")
for alphabets in string:
    print(alphabets,"=",string.count(alphabets),"times")
