import random

class Game:
    Tokens = (20)
    Die = (1)

class Tokens:
    def __init__(self, begin_tokens):
        self.total = begin_tokens

    def win(self, amount):
        self.total += amount

    def lose(self, amount):
        self.total -= amount

class Die:

    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        x = random.randint(1, self.faces)
        return x
