import random

print 'Welcome to the random number guessing game!'


print "Too bad. So sad."

def pick_random_number():
    our_number = random.randint(1, 100)

    return our_number


random_number = pick_random_number()


# notes to our self.

guess = raw_input("What is your first guess?\n")
keep_going = True
guess_count = 1


def get_input(question):
    return raw_input(question)


max_tries = 10

while keep_going:
    if guess_count > max_tries:
        keep_going = False
        some_phrase = "You did a terrible job! The real number was %d"
        print some_phrase % random_number

    else:
        user_input_as_a_number = int(guess)
        if user_input_as_a_number == random_number:
            print "yaya!!"
        else:
            if user_input_as_a_number < random_number:
                print "higher!"
                guess = get_input("Try again!\n")
                guess_count += 1
            else:
                print "lower!"
                guess = get_input("Try again!\n")
                guess_count += 1
    #
# print "The number was: ", random_number

