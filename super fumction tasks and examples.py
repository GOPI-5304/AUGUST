# object oriented program notes.py

# super () function : this method is used to assign all the values and and properties are assigned to subclass 

""""
for example : the car is main class and car type is a sub class 
"""

class college:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def declared(self):
        print("name : ",self.name)
        print("age :",self.age)

class pharmacy(college):
    def __init__(self,name,age,course,percentage):
        super().__init__(name,age)
        self.course=course
        self.percentage=percentage
    def declare_pharmacy(self):
        super().declared()
        print("course :",self.course)
        print("percentage :",self.percentage)
class section(pharmacy):
    def __init__(self,name,age,course,percentage,adm_no,section):
        super().__init__(name,age,course,percentage)
        self.adm_no=adm_no
        self.section=section
    def declare_section(self):
        super().declare_pharmacy()
        print("admission num : ",self.adm_no)
        print("section : ",self.section)

o=section("gopi","25","B-pharmacy","83.6 %",25268,"topper section")
o.declare_section()


