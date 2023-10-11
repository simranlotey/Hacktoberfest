class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance


def create_account(accounts, account_number):
    if account_number not in accounts:
        accounts[account_number] = BankAccount(account_number)
        return True
    else:
        return False


if __name__ == "__main__":
    accounts = {}

    while True:
        print("\nBank System Operations:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            account_number = input("Enter the account number: ")
            if create_account(accounts, account_number):
                print(f"Account {account_number} created successfully.")
            else:
                print(f"Account {account_number} already exists.")
        elif choice == "2":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the deposit amount: "))
            if account_number in accounts:
                if accounts[account_number].deposit(amount):
                    print(f"Deposit of ${amount} successful. New balance: ${accounts[account_number].get_balance()}")
                else:
                    print("Error: Deposit amount must be greater than 0.")
            else:
                print(f"Error: Account {account_number} does not exist.")
        elif choice == "3":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            if account_number in accounts:
                if accounts[account_number].withdraw(amount):
                    print(f"Withdrawal of ${amount} successful. New balance: ${accounts[account_number].get_balance()}")
                else:
                    print("Error: Invalid withdrawal amount.")
            else:
                print(f"Error: Account {account_number} does not exist.")
        elif choice == "4":
            account_number = input("Enter the account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account {account_number} balance: ${balance}")
            else:
                print(f"Error: Account {account_number} does not exist.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
