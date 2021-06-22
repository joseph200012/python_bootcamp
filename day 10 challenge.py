# Python program to create Bankaccount class 
 
class Bank_Account: 

    def __init__(self): 

        self.balance=0

        print(" Welcome to our Bank  ") 

  

    def deposit(self): 

        amount=float(input("Enter amount to be Deposited: ")) 

        self.balance += amount 

        print("\n Amount Deposited:",amount) 

  

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n Your withdrawal:", amount) 

        else: 

            print("\n Insufficient balance  ") 

  

    def display(self): 

        print("\n Net Balance=",self.balance) 

  
# Driver code 

   
# creating an object of class 

s = Bank_Account() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

#To use inheritance in ecommerce concept
#parent class
class Description:              
    description_name_1 = "This is brought to you by "
  
    #child class
class Products(Description):       
    prod_1 = "Union Bank Of India"
    
obj_1 = Products()          
print(obj_1.description_name_1 +obj_1.prod_1)
