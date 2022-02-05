class Player:
    def __init__(self):
        self.health = 1

    def attack(self):
        option = input("Rock (r), Paper, (p), or Scissors (s): ")
        return option


class Enemy:
    def __init__(self):
        self.health = 1

    def attack(self):
        pass


# player_one = Player()
# player_two = Enemy()

# choice = player_one.attack()
# enemy_choice = "s"
# # if choice in "rps":
# #     print(choice)
# # else:
# #     print("Do you remember the rules?")
# # r > s
# # s > p
# # p > r
# # r = r
# # s = s
# # p = p

# if choice == "r" and enemy_choice == "s":
#     print("you win")
# elif choice == enemy_choice:
#     print("") 
# else:
#     print("you lose")
