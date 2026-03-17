from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_account(self, account_type, account_number, owner_name, initial_balance=0, **kwargs):
        if account_number in self.accounts:
            return False, "Account number already exists"
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, owner_name, initial_balance, **kwargs)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, owner_name, initial_balance, **kwargs)
        else:
            return False, "Invalid account type"
        
        self.accounts[account_number] = account
        return True, f"{account_type.title()} account created successfully"
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        
        if not from_account or not to_account:
            return False, "One or both accounts not found"
        
        # Try to withdraw from source account
        success, message = from_account.withdraw(amount)
        if not success:
            return False, f"Transfer failed: {message}"
        
        # Deposit to destination account
        to_account.deposit(amount)
        return True, f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}"
