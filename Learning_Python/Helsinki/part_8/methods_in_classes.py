class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        if annual_interest>1:
            self.annual_interest = annual_interest/100
        else:
            self.annual_interest = annual_interest
    
    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest
    
    # Method to deposit money
    def deposit(self,amount: float) -> float:
        self.balance += amount
    
    # Method to withdraw money
    def withdraw(self,amount: float) -> float:
        if self.balance>=amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
        
    # Check Balance
    def check_balance(self):
        return self.balance
        
    
    
josey = BankAccount(123 ,"Josey", 122, 5 )
josey.add_interest()
print(josey.balance)

# The class BankAccount is defined in the previous example

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
paulas_account = BankAccount("99999-999", "Paula Pythonen", 1500.0, 0.05)
pippas_account = BankAccount("1111-222", "Pippa Programmer", 1500.0, 0.001)

# Add interest on Peter's and Paula's accounts, but not on Pippa's
peters_account.add_interest()
paulas_account.add_interest()

# Print all account balances
print(peters_account.balance)
print(paulas_account.balance)
print(pippas_account.balance)

# Create an instance of the BankAccount class
account = BankAccount("123456", "Alice", 1000.0, 5)

# Test: Check initial balance
print("Initial Balance:", account.check_balance())  # Expected Output: 1000.0

# Test: Add interest
account.add_interest()
print("Balance after adding interest:", account.check_balance())  # Expected Output: 1050.0

# Test: Deposit money
account.deposit(200)
print("Balance after deposit of 200:", account.check_balance())  # Expected Output: 1250.0

# Test: Withdraw money within balance
account.withdraw(300)
print("Balance after withdrawal of 300:", account.check_balance())  # Expected Output: 950.0

# Test: Withdraw money exceeding balance
account.withdraw(1000)  # Expected Output: "Insufficient balance"
print("Balance after failed withdrawal attempt:", account.check_balance())  # Expected Output: 950.0

# Test: Depositing a negative amount (which shouldn't happen but testing for robustness)
account.deposit(-50)
print("Balance after depositing -50 (should not change):", account.check_balance())  # Expected Output: 950.0

# Test: Check if annual interest converts correctly when entered as a whole number
account2 = BankAccount("654321", "Bob", 1000.0, 0.03)  # Interest entered as a decimal
account2.add_interest()
print("Bob's balance after adding 3% interest:", account2.check_balance())  # Expected Output: 1030.0

# Test: Verify the interest rate conversion
account3 = BankAccount("789012", "Charlie", 2000.0, 5)  # Interest entered as 5
account3.add_interest()
print("Charlie's balance after adding 5% interest:", account3.check_balance())  # Expected Output: 2100.0
