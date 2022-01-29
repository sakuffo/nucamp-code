class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Your password hass been changed to", self.password)


class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


bankuser1 = BankUser("Jane", 'jane@email.com', '123')
