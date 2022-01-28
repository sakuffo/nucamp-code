class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Your password hass been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")

print(user1.password)
user1.change_password("bestpassword")
