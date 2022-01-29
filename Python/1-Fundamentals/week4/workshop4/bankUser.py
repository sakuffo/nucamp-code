# Task 3: Create BankUser subclass
from user import User


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)

    # Task 4: Create BankUser instance methods
    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")
        return

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= float(amount)
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += float(amount)

    # Task 5: Transfer and request money
    def transfer_money(self, reciever, amount):
        print(f"You are transferring ${amount} to {reciever.name}")
        print("Authentication Required")
        if self.request_pin() and self.amount_check(amount, reciever):
            self.withdraw(amount)
            self.show_balance()

            reciever.deposit(amount)
            reciever.show_balance()
            print()
        else:
            print("Invalid Pin. Transaction Cancelled")
            self.show_balance()
            reciever.show_balance()
            return False

    def request_money(self, reciever, amount):
        print(f"You are requesting ${amount} from {reciever.name}")
        print("Authentication Required")
        if self.request_pin() and self.amount_check(amount, reciever):
            if reciever.password == input("Enter your password: "):
                self.withdraw(amount)
                self.show_balance()

                reciever.deposit(amount)
                reciever.show_balance()
                print()
            else:
                print("Invalid Password. Transaction Cancelled")
                self.show_balance()
                reciever.show_balance()
                return False
        else:
            print("Invalid Pin. Transaction Cancelled")
            return False

    def request_pin(self):
        entered_pin = input("Enter your PIN: ")
        if self.pin == entered_pin:
            print("Transfer authorized")
            return True

    def amount_check(self, amount, target_user):
        if (amount > 0) and (amount <= self.balance):
            print(f"You are transferring ${amount} to {target_user.name}")
            return True
        else:
            print("Please enter a valid amount")
