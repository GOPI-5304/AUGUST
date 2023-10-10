# Banking system 
# personal details of account holder 
# deposit amount of account holder
# withdraw amount of account holder 
# view balance 

# personal details of account holder : 

# main class for display personal details of account holder

class user:

    def __init__(self,Name,age,gender,account_number):
        self.name=Name
        self.age=age
        self.gender=gender
        self.account_number=account_number
    def personal_details(self):
        print("personal details of account holder : ")
        print("name :",self.name)
        print("age :",self.age)
        print("gender :",self.gender)
        print("account number :", self.account_number) 

    def deposit(self,amount):
        self.amount=amount
        self.balence=0
        self.balence=self.balence+self.amount
        print("The amount to displayede by : ",self.balence)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balence:
            print("insufficient funds | balance available :",self.balence)
        else:
            self.balence=self.balence-self.amount
            print("account balence after withdrawl :",self.balence)
    def view(self):
        self.personal_details()
        print("account_balence : ",self.balence)

sbi=user("gopi",25,"Male",40532747696)
sbi.personal_details()
sbi.deposit(500)
sbi.withdraw(100)
sbi.view()

