import players
import random
import time


class GameWorld:
    def __init__(self):
        self.player = players.Player()
        self.enemy = players.Enemy()
        self.weapons = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

    def play_round(self, weapon, enemy_weapon):
        print(f'The player selected {weapon}!')
        print('Lets see what the computer selects.......')
        time.sleep(random.randint(1, 3))
        print(f'The enemy selected {enemy_weapon}!')
        time.sleep(1)

    def weapon_select(self, cpu=0):
        if cpu:
            option = random.randint(1, 3)
        else:
            option = input(
                ''' \n ------------------
                    \n Select your weapon!
                    \n ------------------
                    \n Rock (1)
                    \n Paper (2)
                    \n Scissors (3)
                    \n ------------------
                    \n Pick your weapon:  '''
            )

        num_option = int(option)
        translation_dict = {
            1: "rock",
            2: "scissors",
            3: "paper"
        }

        return translation_dict[num_option]
