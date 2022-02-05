import players
import choices


class GameWorld:
    def __init__(self):
        self.player = players.Player()
        self.enemy = players.Enemy()
        self.choices = {
            "rock": choices.Rock(),
            "paper": choices.Paper(),
            "scissors": choices.Scissors()
        }


class Match:
    def __init__(self):
        self.game = GameWorld()
