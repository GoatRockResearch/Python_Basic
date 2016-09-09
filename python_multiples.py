#   Python Exercise: Multiples

# Python Import Modules:
from __future__ import print_function

# Part I: Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use any array to do this exercise.
# Method 1:
print('Method 1:')
for x in range(1, 1001, 2):
    print("Odd - ", x)

# Method 2:
print('Method 2:')
for x in range(1, 1001):
    if x % 2 == 1:
        print("Odd - ", x)

# Part II: Create another program that prints all the multiples of 5 from 5 to 1,000,000.
# Method 1:
print('Method 1:')
for y in range(5, 1000001, 5):
    print("Multiples (x5) - ", y)

# Method 2:
print('Method 2:')
for y in range(5, 1000001):
    if y % 5 == 0:
        print("Multiples (x5) - ", y)

# L|5
