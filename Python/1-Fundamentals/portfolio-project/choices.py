class Choice:
    def __int__(self):
        pass


class Rock(Choice):
    def __int__(self):
        self.name = "rock"
        self.triangle = {
            "paper": False,
            "scissors": True
        }


class Scissors(Choice):
    def __int__(self):
        self.name = "scissors"
        self.triangle = {
            "paper": False,
            "scissors": True
        }


class Paper(Choice):
    def __int__(self):
        self.name = "paper"
        self.triangle = {
            "paper": False,
            "scissors": True
        }
