__author__ = 'KRISTINE'
import random

answer = raw_input("Do you want to play a game?")

raw_input("So sweet. Isn't it fun pretending to have freedom of choice?")

token_start = 20

token_phrase = "I see you have %d tokens. When you double that number, you can leave."
print token_phrase % token_start
raw_input("For each correct guess, you will earn twice as much as you bet.")
print "\nGo ahead. All you have to do is roll the die anc call your number.\n"


def roll_the_dice():
    final_roll = random.randint(1, 6)
    return final_roll

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

dice_roll = roll_the_dice()

some_phrase = "\nThe hooded person behind the counter rolls the dice. You see %d on the table\n"
print some_phrase % dice_roll

reward = bet
loss = bet

if dice_roll == int(guess):
    total_tokens = 2*(int(reward)) + int(token_start)

if dice_roll < int(guess):
    total_tokens = int(token_start) - int(loss)

if dice_roll > int(guess):
    total_tokens = int(token_start) - int(loss)

tally_phrase = "Now you have %d tokens."
print tally_phrase % total_tokens

if total_tokens < 40 > 0:
    roll_again = True
if total_tokens > 40:
    roll_again = False
if total_tokens <= 0:
    roll_again = False

while roll_again:
    if 0 < total_tokens < 40:
        print "Go on and try again. I insist."

        go_ahead = True
        place_bets = False

        while go_ahead:
            guess = raw_input("Which number do you bet on?")
            try:
                guess = int(guess)
            except ValueError:
                print "You insist on wasting your time like this?"
            if int(guess) < 1:
                print "Don't be a fool. %d is not on a die." % int(guess)
            if int(guess) > 6:
                print "Don't be a fool. %d is not on a die." % int(guess)
            if 0 < int(guess) < 7:
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
            if bet > total_tokens:
                print "One cannot risk what they do not have."
            if 0 < bet < (total_tokens + 1):
                place_bets = False

        dice_roll = roll_the_dice()

        some_phrase = "\nThe hooded person behind the counter rolls the dice. You see %d on the table\n"
        print some_phrase % dice_roll

        reward = bet
        loss = bet

        if dice_roll == int(guess):
            total_tokens = 2*(int(reward)) + int(total_tokens)

        if dice_roll < int(guess):
            total_tokens = int(total_tokens) - int(loss)

        if dice_roll > int(guess):
            total_tokens = int(total_tokens) - int(loss)

        tally_phrase = "Now you have %d tokens."
        print tally_phrase % total_tokens

    elif total_tokens > 40:
        roll_again = False
        print 'Consider yourself a lucky one. For today.'
    elif total_tokens is 0:
        roll_again = False
        print "Don't forget to lock your doors at night."