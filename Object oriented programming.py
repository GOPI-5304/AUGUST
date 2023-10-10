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


# example 4: 

class car:
    def __init__(self,color,max_speed,accelaration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.accelaration=accelaration
        self.tyre_friction=tyre_friction

van=car(color="bluish white",max_speed="240 km/hour",accelaration=20,tyre_friction=4)
print(van.color)
print(van.max_speed)
print(van.accelaration)
print(van.tyre_friction)
print(van.__dict__)



class car:
    def __init__(self,color,max_speed,accelaration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.accelaration=accelaration
        self.tyre_friction=tyre_friction

    def engine_started(self):
        self.is_engine_started=True
    
    def engine_stop(self):
        self.is_engine_stop=False


van=car(color="bluish white",max_speed=240,accelaration=20,tyre_friction=25)
van.engine_started()
print(van.is_engine_started)
van.engine_stop()
print(van.is_engine_started)


class cart:
    def __init__(self):
        self.items={}

    def add_items(self,name,price,quantity):
        self.items["mobile name"]=name
        self.items["price"]=price
        self.items["quantity"]=quantity
    def get_items(self):
        print(self.items)

result=cart()
result.add_items("oppo mobile",25000,5)
result.get_items()