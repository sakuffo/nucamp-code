def login(database, username, password):
    if username in database:
        if database[username] == password:
            return True
        else:
            print("Incorrect password")
    if username not in database:
        print("User not found")

    return False


def login_check(authorized_user):
    if authorized_user != "":
        print("\nYou are logged in as: " + authorized_user)
    else:
        print("\nYou must be logged in to donate")
