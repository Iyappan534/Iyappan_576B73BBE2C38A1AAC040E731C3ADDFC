class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount
        return f"${amount} deposited successfully. New balance is ${self.__account_balance}"

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn successfully. New balance is ${self.__account_balance}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #: {self.__account_number}): ${self.__account_balance}"

# Creating an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Testing deposit functionality
print(account.deposit(500))  # Output: $500 deposited successfully. New balance is $1500

# Testing withdraw functionality
print(account.withdraw(200))  # Output: $200 withdrawn successfully. New balance is $1300
print(account.withdraw(1500)) # Output: Insufficient funds

# Displaying the account balance
print(account.display_balance())  # Output: Account Balance for John Doe (Account #: 123456789): $1300
