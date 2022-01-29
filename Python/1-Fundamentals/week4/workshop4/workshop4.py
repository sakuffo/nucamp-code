# Task 1: Create a class called User.

class User:

    def __init__(self, name, pin, password):
        pass

    # Task 2: Create User Class instance methods
    def change_name():
        pass

    def change_pin():
        pass

    def change_password():
        pass

# Task 3: Create BankUser subclass


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)

    # Task 4: Create BankUser instance methods
    def show_balance():
        pass

    def withdraw():
        pass

    def deposit():
        pass

    # Task 5: Transfer and request money
    def transfer_money():
        pass

    def request_money():
        pass
