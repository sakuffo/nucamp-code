from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, login_check

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    login_check(authorized_user)

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        login(database, username, password)
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        # register(database, username, password)
        print('TODO: Write Register code')
    elif choice == "3":
        print('TODO: Write Donate code')
    elif choice == '4':
        print('TODO: Write Show Donations code')
    elif choice == '5':
        print('Leaving DonateMe...')
        break
    else:
        print("Invalid option")
