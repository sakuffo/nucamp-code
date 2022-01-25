def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("\nWelcome back " + username + "!")
            return username
        else:
            print("\nIncorrect password for " + username)
            return ""
    if username not in database:
        print("\nUser not found. Please Register")

    return ""


def register(database, username, password):
    if username not in database:
        database[username] = password
        print("\nUsername " + username + " registered!")
        return username
    else:
        print("\nUsername already registered")

    return ""


def login_check(authorized_user):
    if authorized_user != "":
        print("\nYou are logged in as: " + authorized_user)
    else:
        print("\nYou must be logged in to donate")
