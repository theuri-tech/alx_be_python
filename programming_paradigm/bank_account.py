
class BankAccount():
    
    def __init__ (self, account_balance=0):
        self.account_balance = account_balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            #print(f"Deposited {amount}. New balance is {self.account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            #print(f"Withdrawn {amount}. New balance is {self.account_balance}")
            return True
        else:
            #print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")
    
    
        
    