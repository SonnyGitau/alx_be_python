# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # encapsulated with a single underscore

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._account_balance:
            return False
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self._account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

    def get_balance(self):
        """Getter method for unit testing or external read access."""
        return self._account_balance
