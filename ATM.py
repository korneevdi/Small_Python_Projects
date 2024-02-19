"""
This simple program shows how an ATM works.
First of all, it helps entry-level developers understand how to work in the object-oriented programming paradigm, create and use classes.
"""

class MoneyMachine:
    def __init__(self):
        self.balance = 50000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposited {amount} euro")
            self.display_balance()
        else:
            print("The deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew {amount} euro")
            self.display_balance()
        elif amount > self.balance:
            print("Insufficient funds in the account.")
        else:
            print("The amount to withdraw must be positive and not more than your balance.")

    def display_balance(self):
        print(f"Current balance: {self.balance} euro")


atm = MoneyMachine()

print("""
Welcome to ATM Machine

Choose Transaction

1 - BALANCE
2 - WITHDRAW
3 - DEPOSIT
4 - EXIT

""")

option = int(input("Enter Transaction "))

if(option == 1):
    atm.display_balance()
elif(option==2):
    amount = float(input("Enter amount to withdraw "))
    atm.withdraw(amount)
elif(option==3):
    amount = float(input("Enter amount to deposit "))
    atm.deposit(amount)
elif(option==4):
    exit()
else:
    print("no selected transaction")








    
