class BankAccount:
    # constructor that takes in account_name and starting_balance
    def __init__(self, account_name, starting_balance):
        # store account_name and balance as instance fields
        self.account_name = account_name
        self.balance = starting_balance

    # method to deposit some amount of money into the account
    def deposit(self, amount):
        self.balance += amount

    # method to withdraw money from the account
    def withdraw(self, amount):
        self.balance -= amount

    # method to get the current balance of the account
    def get_balance(self):
        # return a string that says "{account_name} has a balance of {balance}"
        return f"{self.account_name} has a balance of {self.balance}"
