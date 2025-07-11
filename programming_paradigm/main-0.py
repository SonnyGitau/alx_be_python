# main.py

import sys
from bank_account import BankAccount

def main():
    # Adjust the initial balance to test different scenarios
    account = BankAccount(200)  # starting with $200 for more flexibility

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_args = sys.argv[1].split(':')
    command = command_args[0].lower()
    amount = float(command_args[1]) if len(command_args) > 1 else None

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
            account.display_balance()

        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
            account.display_balance()

        elif command == "display":
            account.display_balance()

        else:
            print("Invalid command.")
            print("Usage: python main.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
