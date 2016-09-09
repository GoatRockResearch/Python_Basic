#   Python Exercise: Multiply

# Python Import Modules:
from __future__ import print_function

# 1. Create a function called 'multiply';
# 2. Function reads each value in the list: a = [2, 4, 10, 16];
# 3. Function returns a list where each value has been multiplied by 5.
# 4. Function should multiply each value in the list by the second argument:
#   If:
#       a = [2,4,10,16];
#   Then:
#       b = multiply(a, 5);
#   print b should return: [10, 20, 50, 80 ].

# Method 1:
print('Method 1:')
a = [2,4,10,16]
def multiply(alist,multiplier):
    retlist = []
    for index in range(0,len(alist)):
        retlist.append(alist[index] * multiplier)
    return retlist
print('Base List:', a)
print('List Multiplied x5:',multiply(a,5))

# L|5
