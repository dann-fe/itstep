class BankAccount:
    def __init__(self, owner: str, balance: float = 0.00):
        self.owner = owner
        self.balance = float(balance)
    
    def deposit(self, amount: float):
        if amount > 0.00:
            self.balance += amount
            print(f'You deposited {amount} to your account. Your balance is now {self.balance}')
        else:
            raise ValueError("Amount deposited should be greater than 0")

    def withdraw(self, amount: float):
        if amount > 0.00 and amount <= self.balance:
            self.balance -= amount
            print(f'You withdrew {amount} from your account. Your balance is now {self.balance}')
        else:
            raise ValueError(f"The amount cannot be bigger than your account balance and smaller than 0.01")
        
    def viewbalance(self):
        return f"Current balance: {self.balance}"

my_account = BankAccount("dan", 1000.00)
my_account.withdraw(1000)

print(my_account.viewbalance())