from account import Account
from transaction import Transaction

class SavingsAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.01, min_balance=100):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        
        if self.balance - amount < self.min_balance:
            return False, f"Cannot withdraw below minimum balance of ${self.min_balance:.2f}"
        
        self.balance -= amount
        transaction = Transaction("withdrawal", amount, self)
        self.transaction_history.append(transaction)
        return True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        transaction = Transaction("interest", interest, self)
        self.transaction_history.append(transaction)
        return True, f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}"
