class Transaction:
    def __init__(self, transaction_type, amount, account):
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account
    
    def __str__(self):
        return f"{self.transaction_type.title()} - ${self.amount:.2f}"
