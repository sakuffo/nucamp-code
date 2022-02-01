# Task 1: Create a class called User.
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        self.balance = 0

    # Task 2: Create User Class instance methods
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password