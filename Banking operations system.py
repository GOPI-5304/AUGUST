# Banking operstion system


class user():
    name="GOPI 5304"
    password="gopiprince@5304"
    def create_account(self):
       print("enter details of account holder")
       self.name=input("enter name : ")
       self.age=input("enter age : ")
       self.gender=input("enter gender : ")
       self.address=input("enter address of holder : ")
       self.account_number=input("enter account number : ")
       print("Account created successfuly")
class banking(user):
    balence=0
    def deposit(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            self.amount=int(input("enter deposited amount : "))
            self.balence=self.balence+self.amount
            print("The deposited amount is : ",self.balence)
        else:
            print("invalid user name or password")

    def withdraw(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            self.amount=int(input("enter withdrwal amount : "))
            if self.amount>self.balence:
                print("insufficient funds | Available balence is: ",self.balence)
            else:
                self.balence=self.balence-self.amount
                print("account balence after withdrawl :",self.balence)
        else:
            print("invalid user name or password")
    
    def display_balance(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            print("The available balance is : ",self.balence)
        else:
            print("invalid user name or password")

bank=banking()
print("---select options below---")
print()
while True:
    user_option=input("enter option : ")
    if user_option=="1":
        bank.create_account()
    elif user_option=="2":
        bank.deposit()
    elif user_option=="3":
        bank.withdraw()
    elif user_option=="4":
        bank.display_balance()
    else:
        print("invalid option")
    next_step=input("enter yes or no for next option : ")
    if next_step=="yes":
        continue
    else:
        break