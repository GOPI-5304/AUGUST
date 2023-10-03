
d={}
list=[]
n=int(input("enter no of employees you want : "))
for i in range(1,n+1):
    print("employee number :- ",i)
    d["name"]=input("enter name : ")
    d["emp id"]=input("enter emp id : ")
    d["designation"]=input("enter designation : ")
    d["e mail"]=input("enter email id : ")
list.append(d)
print(list)
print("employee",i, "added successfully")

all_details=input("for adding details type add and for remove type remove and print details type Print :  ")
if all_details=="add":
    dictionaries=input("add existed elemnt type EX and add new items type NI : ")
    if dictionaries=="EX":
        details=input("Type name:N,emp id:E,designation:D,email:EM")
        name=input("enter existed details : ")
        if details=="N":
            d["name"]=(name)
            result=d
        elif details=="E":
            d["emp id"]=(name)
            result=d
        elif details=="D":
            d["designation"]=(name)
            result=d
        elif details=="EM":
            d["e mail"]=(name)
            result=d
            print(result)
        else:
            print(name,"is not found")
    
    elif dictionaries=="NI":
        items=input("add items : ")
        name=input("enter value of the new item : ")
        d[items]=name
        print("newly added element is ",d)
   
elif all_details=="remove":
    value=input("for one delete type d for one delete  type de : ")
    if value=="d":
        name=input("enter attribute which you want to delete : ")
        d.pop(name)
        for details in d.items():
            print(details)
    elif value=="de":
        deleted=d.clear()
        print(deleted)
    else:
        print(value,"no attribute should be found")

elif all_details=="print":
        details=input("enter only one attribute type O and print all details type De : ") 
        if details=="O":   
            name=input("enter attribute name : ")
            if name in d:
                column=d.get(name)
                print(column)
            else:
                print("No attribute should be found")
        elif details=="De":
            list.append(d)
            for details in list:
                print(details)
        else:
            print("details not found ")

