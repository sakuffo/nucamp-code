from bankUser import BankUser


""" Driver Code for Task 1 """
# bob = User("Bob", "1234", "password")
# print(f"{bob.name} {bob.pin} {bob.password}")

""" Driver Code for Task 2 """
# tom = BankUser("Tom", "4321", "password")
# print(f"{tom.name} {tom.pin} {tom.password}")
# tom.change_name("Tommy")
# tom.change_pin("54321")
# tom.change_password("new_password")
# print(f"{tom.name} {tom.pin} {tom.password}")

""" Driver Code for Task 3 """
# esi = BankUser("Esi", "1234", "password")
# print(f"{esi.name} {esi.pin} {esi.password} {esi.balance}")

""" Driver Code for Task 4 """
# akosua = BankUser("akosua", "1234", "password")
# akosua.show_balance()
# akosua.deposit(1000)
# akosua.show_balance()
# akosua.withdraw(500)
# akosua.show_balance()

""" Driver Code for Task 5 """

# create both users and initialize their balances
kofi = BankUser("Kofi", "1234", "kpass")
kofi.deposit(5000)
ibrahim = BankUser("Ibrahim", "1234", "ipass")
kofi.show_balance()
ibrahim.show_balance()
print()
# transfer money from kofi to ibrahim'
kofi.transfer_money(ibrahim, 500)
ibrahim.request_money(kofi, 250)
