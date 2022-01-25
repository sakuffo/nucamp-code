def show_homepage():
    print("")
    print("          === DonateMe Hompage ===       ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.  Register       |")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("|               5.    Exit               |")
    print("------------------------------------------")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_amt = float(donation_amt)
    donation = f"{username} donated ${donation_amt}"
    print(donation)
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    if donations == []:
        print("Currently, there are no donations.")
    else:
        print("")
        print("          === Donations ===       ")
        print("------------------------------------------")
        for donation in donations:
            print(donation)
        print("------------------------------------------")
        print("")
