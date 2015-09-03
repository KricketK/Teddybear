__author__ = 'Kricket'

answer = raw_input("Do you want to play a game?")

raw_input("So sweet. Isn't it fun pretending to have freedom of choice?")


class Tokens:
    def __init__(self, begin_tokens):
        self.total = begin_tokens

    def win(self, amount):
        self.total += amount

    def lose(self, amount):
        self.total -= amount



token_phrase = "I see you have %d tokens. When you double that number, you can leave."
print token_phrase % token_start

raw_input("For each correct guess, you will earn twice as much as you bet.")
print "\nGo ahead. All you have to do is roll the die anc call your number.\n"