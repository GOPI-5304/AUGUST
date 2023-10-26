# HOSPITAL MANAGEMENT SYSTEM

class HospitalSystem:
    def __init__(self):
        self.list=[]
    
class patient(HospitalSystem):
    def add_patient_details(self):
        num=int(input("enter no of patient to add : "))
        for i in range(1,num+1):
            self.d={}
            self.d["id"]=int(input("enter patient id : "))
            self.d["name"]=input("enter name : ")
            self.d["age"]=int(input("enter age :"))
            self.d["gender"]=input("enter gender :")
            self.d["ph.no"]=input("enter mobile number :")
            self.d["address"]=input("enter address :")
            self.list.append(self.d)
            print("The patient details added successully")
    
    def print_details(self):
        for details in self.list:
            print(details)
    
    def search_patient_details_by_id(self):
        id=int(input("enter searched id : "))
        for details in self.list:
            if details["id"]==id:
                print(details)
            else:
                None
    def remove_patient_details_by_id(self):
        id=int(input("enter removed id : "))
        for details in self.list:
            if details["id"]==id:
                self.list.remove(details)
                print(f"The id of {id} removed successfully ")
                print(self.list)
            else:
                print(f"The details{id} not found to remove ")
    def update_patient_details_by_id(self):
        id=int(input("enter updated id : "))
        for details in self.list:
            if details["id"]==id:
                update_element=input("enter update element : ")
                if update_element=="name":
                    details["name"]=input("enter name : ")
                    print(details)
                elif update_element=="age":
                    details["age"]=int(input("enter updated age : "))
                    print(details)
                elif update_element=="gender":
                    details["gender"]=input("enter gender : ")
                    print(details)
                elif update_element=="mobile number":
                    details["ph.no"]=int(input("enter mobile number : "))
                    print(details)
                elif update_element=="address":
                    details["address"]=input("enter address : ")
                    print(details)
                else:
                    print(f"The {update_element} was not found ! ")
                    print("Try with valid element")
                    s=input("press any key to exit : ")
            else:
                None


o=patient()
while True:
    print("add")
    print("print")
    print("search")
    print("delete")
    print("update")
    print()
    input_user=input("select the function : ")
    print()
    if input_user=="add":
        o.add_patient_details()
    elif input_user=="print":
        o.print_details()
    elif input_user=="search":
        o.search_patient_details_by_id()
    elif input_user=="delete":
        o.remove_patient_details_by_id()
    elif input_user=="update":
        o.update_patient_details_by_id()
    else:
        print("Type the valid element to run the functions ")
    
    next_user=input("type yes/no for further step : ")
    if next_user=="yes":
        continue
    else:
        break     
