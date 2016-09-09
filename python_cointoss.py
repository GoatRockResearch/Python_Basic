#   Python Exercise: Coin Toss

# Python Import Modules:
from __future__ import print_function
import random

# Instructions:
# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

# Sample output should be like the following:
    # Starting the program...
    # Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
    # Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
    # Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
    # Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
    # Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
    # Ending the program, thank you!

# Here are some hints that might help:
    # 1. Use the python random module to generate a random number
        # import random
        # random_num = random.random()
    # 2. The random function will return a floating point number,
        # that is 0.0 <= random_num < 1.0

# 2. Use the python built-in round function to convert that floating point number into an integer
    # x = .23945593
    # y = .798839238
        # x_rounded will be rounded down to 0
    # x_rounded = round(x)
        # y_rounded will be rounded up to 1
    # y_rounded = round(y)


# f(x) definition
def cointoss():
    # variables
    heads = 0
    tails = 0
    # range parameter attempt
    for attempt in range(1,5001):
        # generate random float number, round number, convert float to integer
        coinflip = int(round(random.random()))
        # check flip for heads(1)/tails(0)
        # head check
        if coinflip == 1:
            heads += 1
            thistoss = 'Heads'
        # tail check
        else:
            tails += 1
            thistoss = 'Tails'
        # print flip result
        print('Coin Flip: Attempt #{}; Coin Flip Result: {}. Total: {} Heads and {} Tails.'.format(attempt, thistoss, heads, tails))
# call f(x)
cointoss()

# L|5
