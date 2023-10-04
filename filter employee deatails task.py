
employees = {}
def add_employees():
    name = input("enter the employee name: ")
    empid = input("enter the employee id: ")
    email = input("enter the employee email id: ") 
    designation = input("enter the employee designation: ")
    employees[name] = {'empid':empid, 'emailid':email, 'designation':designation}
    print(employees)


def stored_employees():
    name=input("enter type attribute to display employees : ")
    found=False
    for key,value in employees.items():
        if (value["designation"])==name:
            print(key,value)
            found=True
        elif (value["emailid"])==name:
            print(key,value)
            found=True
        elif (value["empid"])==name:
            print(key,value)
            found=True
        else:
            print("the attribute is not in employees")
    if not found:
        print("not found with this designation")

num=int(input("enter no of employees : "))
for i in range(1,num+1):
    add_employees()
print("employee details added successfully : ")

stored_employees()