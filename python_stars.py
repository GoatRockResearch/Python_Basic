#   Python Exercise: Stars

# Python Import Modules:
from __future__ import print_function

# Instructions:
# Part 1
# 1. Create a function called  draw_stars() that takes a list of numbers and prints out  *.
# For example:
    # x = [4, 6, 1, 3, 5, 7, 25]

# draw_stars(x) should print the following in when invoked:
    # ****
    # ******
    # *
    # ***
    # *****
    # *******
    # *************************

# Part 2
# 2. Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
# For example:
    #  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# draw_stars(x) should print the following in the terminal:
    # ****
    # ttt
    # *
    # mmmmmmm
    # *****
    # *******
    # jjjjjjjjjjj

# Part 1
# f(x) stars
def draw_stars(xlist):
    for number in xlist:
        print('*' * number)
# List
x = [4, 6, 1, 3, 5, 7, 25]
# f(x) call
draw_stars(x)

# Part 2
# print divider
print('-----')
# f(x) letters
def draw_strings(ylist):
    # loop
    for item in ylist:
        # check for integer and print * x length of item
        if (type(item) == int):
            print('*' * item)
        # check for string and print first letter, lowercase, x length of item
        elif (type(item) == str):
            print(item[0].lower() * len(item))
# List
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# print list for check
print('List:', y)
# print divider
print('-----')
# f(x) call
draw_strings(y)

# L|5
