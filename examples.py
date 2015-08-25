class Glass:
    size = 0
    clarity = "clear"
    max_volume = 0
    current_volume = 0

    def __init__(self, max_volume):
        self.max_volume = max_volume

    def fill(self, volumn_amt):
        if volumn_amt > self.max_volume:
            print 'overflowed!!'
            self.current_volume = self.max_volume
        else:
            self.current_volume = volumn_amt

    def pour(self, amount):
        if amount > self.current_volume:
            self.current_volume = 0
        else:
            self.current_volume -= amount


class Cat:
    def __init__(self, name, color, attackPower):
        self.name = name
        self.color = color
        self.attackPower = attackPower


    def walk(self):
        pass

    def jump(self):
        pass

    def actLikeAfuckingShit(self):
        pass

    def attack(self, otherCat):
        print "im going to fuck up that cat", otherCat.name
        if self.attackPower > otherCat.attackPower:
            print "I kicked his fucking ass!!"
        else:
            print 'RUN AWAY!!!'


    def speak(self, volume):
        if volume > 5:
            print "MY NAME IS", self.name.upper()
        else:
            print "my name is", self.name

import random

class Bank:
    def __init__(self, starting_tokens):
        self.total = starting_tokens

    def add_tokens(self, amount):
        self.total += amount

    def sub_tokens(self, amount):
        self.total -= amount


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        randint = random.randint(1, self.sides)
        print "I rolled a ", randint, "on a ", self.sides, "'d die"
        return randint


class D6(Die):
    def __init__(self):
        Die.__init__(self, 6)

class D20(Die):
    def __init__(self):
        Die.__init__(self, 20)

class Game:

    bank = None
    dice = None
    players = []

    def __init__(self, starting_bank, num_of_die):
        self.bank = Bank(starting_bank)

        self.dice = [Die(6) for die in range(num_of_die)]

    def roll(self):
        total = 0

        for die in self.dice:
            roll = die.roll()

            total += roll

        print total
