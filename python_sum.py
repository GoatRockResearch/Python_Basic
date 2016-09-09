#   Python Exercise: Sum

# Python Import Modules:
from __future__ import print_function

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
# Method 1
print('Method 1:')
a = [1, 2, 5, 10, 255, 3]
total = 0
for val in a:
    total = total + val
print(total)
print('=====')

# Method 2
print('Method 2:')
a = [1, 2, 5, 10, 255, 3]
total = 0
for val in a:
    total += val
print(total)
print('=====')

# Method 3
print('Method 3:')
def a(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum
print(a([1, 2, 5, 10, 255, 3]))
print('=====')

# Method 4: Check val in x
print('Method 4:')
x = ['Hello Coder', 1, 2, 5, 10, 255, 3, 'Later Ninja']
tsum = 0
for val in x:
    if type(val) == int:
        tsum += val
    else:
        print ('Check Type:',val, 'is not an integer, cannot add to sum of array.')
        continue
print('-----')
print('List Value:',x)
print('List Sum:',tsum)

# L|5
