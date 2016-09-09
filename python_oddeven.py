#   Python Exercise: Odd & Even

# Python Import Modules:
from __future__ import print_function

#   1: create a python function that counts from 1 to 2000 using a loop;
#   2: function count returns number;
#   3: function determines odd/even of said number;
#   4: output:
#       'Number is {x}.  This is an {odd/even} number'.

# Method 1:
print('Method 1:')
def odd_even():
    for num in range(1,2001):
        if num % 2 == 1:
            numtype = 'odd'
        else:
            numtype = 'even'
        print('Number is {}. This is an {} number.'.format(num,numtype))
odd_even()

# L|5
