import players
import random


class GameWorld:
    def __init__(self):
        self.player = players.Player()
        self.enemy = players.Enemy()
        self.weapons = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

    def weapon_select(self, cpu=0):
        if cpu:
            option = random.randint(1, 3)
        else:
            option = input(
                '''
                    Select your weapon!\n
                    Rock (1)\n
                    Paper (2)\n
                    Scissors (3)\n 

                    -- 
                '''
            )

        num_option = int(option)
        translation_dict = {
            1: "rock",
            2: "scissors",
            3: "paper"
        }

        return translation_dict[num_option]
