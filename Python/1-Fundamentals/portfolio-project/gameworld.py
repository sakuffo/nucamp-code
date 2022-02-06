import players


class GameWorld:
    def __init__(self):
        self.player = players.Player()
        self.enemy = players.Enemy()
        self.weapons = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
