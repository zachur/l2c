class BankAccount:
    # Constructor with private and protected attributes
    def __init__(self, account_holder, balance):
        # Private attribute (can only be accessed within the class)
        self.__account_holder = account_holder
        # Protected attribute (can be accessed within the class and its subclasses)
        self._balance = balance

    # Public method to display account information
    def display_account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ${self._balance:.2f}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit of ${amount:.2f} successful.")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Creating an instance of the BankAccount class
account1 = BankAccount("John Doe", 1000.0)

# Attempting to access private and protected attributes directly (will result in an error)
# print(account1.__account_holder)  # Uncommenting this line will raise an AttributeError
# print(account1._balance)          # Uncommenting this line is allowed but against convention

# Accessing attributes and methods through public interface
account1.display_account_info()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_account_info()
