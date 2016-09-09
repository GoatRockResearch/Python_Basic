#   Python Exercise: Average

# Python Import Modules:
from __future__ import print_function

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
# Method 1:
print('Method 1:')
a = [1, 2, 5, 10, 255, 3]
total = 0
listlen = len(a)
for val in a:
    total += val
print('List Length:',listlen)
print('List Average:',total/listlen)
print('=====')

# Method 2:
print('Method 2:')
x = ['Hello Coder',1, 2, 5, 10, 255, 3,'Later Ninja']
tsum = 0
listlenavg = 0
for val in x:
    if type(val) == int:
        listlenavg += 1
        tsum += val
    else:
        print ('Check Type:',val, "is not an integer, cannot add to average of array.")
        continue
print('-----')
print('List Length:',listlen)
print('List Average:',tsum/listlenavg)



# Method 3:
# a = [1, 2, 5, 10, 255, 3]
# print reduce(lambda x, y: x + y, a) / len(a)

# L|5
