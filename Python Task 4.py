
# write a python program that allows you to add an employee with domain, name, empid, and email details using user input and then print the employee's details

# taken the empty list 

details=[]
def add():
    global details
    n=int(input("no of employees taken : "))
    for employes in range(1,n+1):
        d={}
        d["name"]=input("name : ")
        d["emp id"]=input("emp id : ")
        d["domain"]=input("domain : ")
        d["email"]=input("e mail : ")
    details.append(d)
    print()
    print()

def remove():
    global details
    n=int(input("Type remove for removing details , type attribute for removing one of column, type delete for clear of details"))
    if n=='remove':
        char=input("enter a attribute to remove employee : ")
        for i in details:
            if char == i.get('name') or (char == i.get('emp id') or (char == i.get('domain') or char == i.get('email'))):
                details.remove(i)
                break
            else:
                print("attribute is not found")
    elif n=='attribute':
        char=input("enter which attributre shoud be removed")
        for i in range(len(details)):
            if char== details[i].get('name') :
                details[i].pop('name') 
                break
            elif char==details[i].get('emp id'):
                details[i].pop('emp id')
                break
            elif char==details[i].get('domain'):
                details[i].pop('domain')
                break
            elif char==details[i].get('e mail'):
                details[i].pop('e mail')
        else:
            print("employee with given attribute is not found")
        
        print()
        print()
    elif n=='delete':
        details.clear()

    print()
    print()

def print_details():
    global details
    n=input("type e for only employee details , type p for all details of employees ")
    if n=='e':
        char=input("attribute name : ")
        for i in details:
            if char == i.get('name') or (char == i.get('emp id') or (char == i.get('domain') or char == i.get('e mail'))):
                print(i) 
        else:
            print("given atribute is not found")
        print()
        print()

    elif n=='p':
        print(details)
        print()
        print()
        
def condition():
    n=input('to add type a, to remove type r, to print type p : ')
    if n=='a':
        add()
    elif n=='r':
        remove()
    elif n=='p':
        print_details()
    print()
    condition()
        



























    
