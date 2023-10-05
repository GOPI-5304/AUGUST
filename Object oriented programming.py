# add employee details and filter employee details 


# Get the details by by using oops :
# example 1:
class mobile:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def get_details(self):
        self.age="55"

obj=mobile("gopi","36","male")
print(obj.__dict__)

# Accessing the values in class :
class car:
    def __init__(self):
        self.car_name="maruthgi 800"
        self.color="bluish black"
        self.car_price="1,50,000"
        self.car_type="family car"

obj=car()
print(obj.car_name)

#  update the values in class :

class car:
    def __init__(self):
        self.car_name="maruthgi 800"
        self.color="bluish black"
        self.car_price="1,50,000"
        self.car_type="family car"
        
    def updated_details(self):
        self.car_name="fortuner"
        self.color="white"
        self.car_price="14 lakhs"
        self.car_type="suv"


obj=car()  # refereence object should transfer the values to another reference object 
print(obj.car_type)
print(obj.__dict__)
obj.updated_details()
print(obj.car_name)
print(obj.__dict__)


# Delete the attribute and value from class:

class employee:
    def __init__(self):
        self.name="gopi prince"
        self.age="32"
        self.domain="python"
        self.email="gopiprince09901@gamail.com"
        del self.name

obj=employee()
print(obj.__dict__)