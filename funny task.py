# Funny task : reverse the input names by different ways

name=input("enter name : ")
length=len(name)
rev=name[::-1]
splitting=name.split()
output=" ".join(reversed(splitting))
rev1=output[::-1]
print(rev)
print(output)
print(rev1)

