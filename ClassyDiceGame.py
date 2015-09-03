__author__ = 'Kricket'

import random

answer = raw_input("Do you want to play a game?")

raw_input("So sweet. Isn't it fun pretending to have freedom of choice?")


class User:
    def __init__(self, name):
        self.name = name

    def guess(self, attempt):
        self.attempt = attempt

    def bet(self, choice):
        self.choice = choice

#now we need to determine the username

player = User(raw_input("What is your name?"))
try:
    player = str(player)
except ValueError:
    print "That's a terrible name. Pick a new one. One made from letters."
else:
    print "So nice to meet you," + player + "."

class Tokens:
    def __init__(self, begin_tokens, total):
        self.begin_tokens = begin_tokens
        self.total = total

    def win(self, amount):
        self.total += 2*amount

    def lose(self, amount):
        self.total -= amount

User.name = Tokens(20, 20)

token_start = User.name.begin_tokens

token_total = User.name.total

token_phrase = "I see you have %d tokens. When you double that number, you can leave."
print token_phrase % User.name.begin_tokens

raw_input("For each correct guess, you will earn twice as much as you bet.")
print "\nGo ahead. All you have to do is roll the die anc call your number.\n"

roll_again = False
go_ahead = True
place_bets = False


while go_ahead:
    guess = raw_input("Which number do you bet on?")
    try:
        guess = int(guess)
    except ValueError:
        print "You insist on wasting your time like this?"
    else:
        if guess < 1:
            print "Don't be a fool. That is not on a die."
        elif guess > 6:
            print "Don't be a fool. That is not on a die."
        elif 0 < guess < 7:
            go_ahead = False
            place_bets = True

while place_bets:
    bet = raw_input('And how much do you want to bet on that?')
    try:
        bet = int(bet)
    except ValueError:
        print "This is no game to bet words on."
    if bet < 1:
        print "Something must be risked for something to be gained."
    if bet > token_start:
        print "One cannot risk what they do not have."
    if 0 < bet < (token_start + 1):
        place_bets = False
        roll_again = True


class Die:

    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        x = random.randint(1, self.faces)
        return x