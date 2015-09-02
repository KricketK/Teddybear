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


class KrickettDie:
    def __init__(self, sides):
        self.sides = sides
        self.currentTry = 0
        self.loadOnTry = random.randint(1, 7)
        print "Imma cheat on the " + str(self.loadOnTry + 1) + " roll"

    def roll(self):
        if self.currentTry == self.loadOnTry:
            print "fucking cheat!!"
            self.currentTry = 0
            return 1
        else:
            self.currentTry += 1
            return random.randint(1, self.sides)


class Loaded(Die):
    def roll(self):
        return self.sides


class Shaker:
    def __init__(self, dice):
        self.dice = dice

    def roll(self):
        x = 0
        for d in self.dice:
            x += d.roll()
        return x
