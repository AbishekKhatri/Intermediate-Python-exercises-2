from BankAccount import BankAccount

# instantiate BankAccount class with hardcoded account_name and starting_balance
account = BankAccount("Cristiano Ronaldo", 7777)

# deposit amount
account.deposit(600)

# withdraw amount
account.withdraw(45)

# print the result of calling the get_balance method
print(account.get_balance())
