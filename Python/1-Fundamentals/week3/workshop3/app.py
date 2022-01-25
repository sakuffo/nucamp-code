from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, login_check, register

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
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        register(database, username, password)
    elif choice == "3":
        if authorized_user != "":
            donation = donate(authorized_user)
            donations.append(donation)
    elif choice == '4':
        show_donations(donations)
    elif choice == '5':
        print('Leaving DonateMe...')
        break
    else:
        print("Invalid option")
