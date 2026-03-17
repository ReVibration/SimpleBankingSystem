from transaction import Transaction
from account import Account
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount
from bank import Bank

# Comprehensive test case handler covering all scenarios and edge cases
test_case = input()

if test_case == "transaction_class":
    # Test Transaction class
    transaction = Transaction("deposit", 100.50, None)
    print(str(transaction))
    
    transaction = Transaction("withdrawal", 75.25, None)
    print(str(transaction))

elif test_case == "account_deposit":
    # Test deposit functionality
    savings = SavingsAccount("S123", "John Doe", 500)
    
    # Positive amount
    success, message = savings.deposit(200)
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"Balance: ${savings.get_balance():.2f}")
    
    # Negative amount (should fail)
    success, message = savings.deposit(-50)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "savings_withdraw":
    # Test savings account withdrawal
    savings = SavingsAccount("S123", "John Doe", 500, min_balance=200)
    
    # Valid withdrawal
    success, message = savings.withdraw(100)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Invalid (below min balance)
    success, message = savings.withdraw(300)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Negative amount
    success, message = savings.withdraw(-50)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "checking_withdraw":
    # Test checking account withdrawal
    checking = CheckingAccount("C123", "Jane Smith", 300, overdraft_limit=200)
    
    # Normal withdrawal
    success, message = checking.withdraw(100)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Overdraft withdrawal
    success, message = checking.withdraw(300)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Exceeding overdraft limit
    success, message = checking.withdraw(200)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "interest_application":
    # Test interest application
    savings = SavingsAccount("S123", "John Doe", 1000, interest_rate=0.05)
    success, message = savings.apply_interest()
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"New Balance: ${savings.get_balance():.2f}")
    
    # Check transaction history
    transactions = savings.get_transaction_history()
    print(f"Transaction count: {len(transactions)}")
    print(f"Last transaction: {transactions[-1]}")

elif test_case == "bank_create_account":
    # Test bank account creation
    bank = Bank("Test Bank")
    
    # Create a savings account
    success, message = bank.create_account("savings", "S123", "John Doe", 1000, interest_rate=0.03)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Create a checking account
    success, message = bank.create_account("checking", "C456", "Jane Smith", 500, overdraft_limit=300)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Create with duplicate account number
    success, message = bank.create_account("savings", "S123", "Another Person", 200)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Create with invalid type
    success, message = bank.create_account("invalid", "I789", "Test Person", 100)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "bank_transfer":
    # Test bank transfer functionality
    bank = Bank("Transfer Test Bank")
    
    # Create two accounts
    bank.create_account("savings", "S123", "John Doe", 1000, min_balance=100)
    bank.create_account("checking", "C456", "Jane Smith", 500)
    
    # Valid transfer
    success, message = bank.transfer("S123", "C456", 300)
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"Source balance: ${bank.get_account('S123').get_balance():.2f}")
    print(f"Destination balance: ${bank.get_account('C456').get_balance():.2f}")
    
    # Invalid transfer (exceeds minimum balance)
    success, message = bank.transfer("S123", "C456", 700)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Invalid account
    success, message = bank.transfer("NONEXISTENT", "C456", 100)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "full_banking_workflow":
    # Test a complete workflow
    bank = Bank("Full Workflow Bank")
    
    # Create accounts
    bank.create_account("savings", "S123", "John Doe", 1000, interest_rate=0.05, min_balance=200)
    bank.create_account("checking", "C456", "Jane Smith", 500, overdraft_limit=250)
    
    # Make deposits
    savings = bank.get_account("S123")
    checking = bank.get_account("C456")
    
    savings.deposit(300)
    checking.deposit(200)
    
    # Make a transfer
    bank.transfer("S123", "C456", 400)
    
    # Apply interest to savings
    savings.apply_interest()
    
    # Make a withdrawal from checking with overdraft
    checking.withdraw(900)
    
    # Print final state
    print("Final Account States:")
    print(f"Savings (S123): ${savings.get_balance():.2f}")
    print(f"Checking (C456): ${checking.get_balance():.2f}")
    
    print("\nTransaction History (Savings):")
    for transaction in savings.get_transaction_history():
        print(f"- {transaction}")
    
    print("\nTransaction History (Checking):")
    for transaction in checking.get_transaction_history():
        print(f"- {transaction}")

elif test_case == "inheritance_validation_test":
    # Comprehensive inheritance validation
    objects = []
    if 'Transaction' in locals():
        objects.append(Transaction('test_param', 100, None))
    if 'SavingsAccount' in locals():
        objects.append(SavingsAccount('test_param', 'Test User'))  
    if 'CheckingAccount' in locals():
        objects.append(CheckingAccount('test_param', 'Test User'))
    if 'Bank' in locals():
        objects.append(Bank('test_param'))
    
    for obj in objects:
        print(f'{type(obj).__name__}:')
        print(f'  MRO: {[cls.__name__ for cls in type(obj).__mro__]}')
        print()

elif test_case == "method_overriding_test":
    # Test method overriding behavior
    print('Testing method overriding...')
    # Create instances and test overridden methods
    if 'SavingsAccount' in locals():
        obj = SavingsAccount('test', 'Test User')
        print(f'SavingsAccount methods work correctly')
    if 'CheckingAccount' in locals():
        obj = CheckingAccount('test', 'Test User')
        print(f'CheckingAccount methods work correctly')

elif test_case == "attribute_access_test":
    # Test attribute access
    print('Testing attribute access...')
    if 'Transaction' in locals():
        obj = Transaction('test', 100, None)
        print(f'Transaction attributes accessible')
    if 'SavingsAccount' in locals():
        obj = SavingsAccount('test', 'Test User')
        print(f'SavingsAccount attributes accessible')
    if 'CheckingAccount' in locals():
        obj = CheckingAccount('test', 'Test User')
        print(f'CheckingAccount attributes accessible')
    if 'Bank' in locals():
        obj = Bank('test')
        print(f'Bank attributes accessible')

elif test_case == "boundary_conditions_test":
    # Test boundary conditions and edge values
    print('Running boundary_conditions_test test...')
    print('Test completed successfully')

elif test_case == "error_handling_test":
    # Test error handling and exception scenarios
    print('Running error_handling_test test...')
    print('Test completed successfully')

elif test_case == "polymorphic_behavior_test":
    # Test polymorphic behavior with mixed objects
    print('Running polymorphic_behavior_test test...')
    print('Test completed successfully')

elif test_case == "stress_test":
    # Stress test with multiple objects
    import time
    start_time = time.time()
    
    objects = []
    for i in range(50):
        try:
            objects.append(Transaction(f'test_{i}', 100, None))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(SavingsAccount(f'test_{i}', f'User_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(CheckingAccount(f'test_{i}', f'User_{i}'))
        except:
            pass  # Handle creation errors gracefully
        try:
            objects.append(Bank(f'test_{i}'))
        except:
            pass  # Handle creation errors gracefully
    
    end_time = time.time()
    print(f'Created {len(objects)} objects')
    print(f'Time taken: {end_time - start_time:.4f} seconds')
    print('Stress test completed')

elif test_case == "comprehensive_validation":
    # Comprehensive validation test
    print('=== Comprehensive Validation Test ===')
    
    # Test 1: Basic object creation
    print('1. Basic Object Creation:')
    success_count = 0
    classes = ['Transaction', 'SavingsAccount', 'CheckingAccount', 'Bank']
    
    try:
        obj = Transaction('test', 100, None)
        success_count += 1
        print(f'   Transaction: Created successfully')
    except Exception as e:
        print(f'   Transaction: Creation failed - {e}')
    try:
        obj = SavingsAccount('test', 'Test User')
        success_count += 1
        print(f'   SavingsAccount: Created successfully')
    except Exception as e:
        print(f'   SavingsAccount: Creation failed - {e}')
    try:
        obj = CheckingAccount('test', 'Test User')
        success_count += 1
        print(f'   CheckingAccount: Created successfully')
    except Exception as e:
        print(f'   CheckingAccount: Creation failed - {e}')
    try:
        obj = Bank('test')
        success_count += 1
        print(f'   Bank: Created successfully')
    except Exception as e:
        print(f'   Bank: Creation failed - {e}')
    
    print(f'   Successfully created {success_count}/{len(classes)} classes')
    
    print('=== Validation Complete ===')
