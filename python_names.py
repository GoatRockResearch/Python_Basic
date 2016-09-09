#   Python Exercise: Names

# Python Import Modules:
from __future__ import print_function

# Instructions:
# Part I
# Given the following list:
    # students = [
    #      {'first_name':  'Michael', 'last_name' : 'Jordan'},
    #      {'first_name' : 'John', 'last_name' : 'Rosales'},
    #      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    #      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    # ]
# Create a program that outputs:
    # Michael Jordan
    # John Rosales
    # Mark Guillen
    # KB Tonel

# Part II
# Now, given the following dictionary:
    # users = {
    #  'Students': [
    #      {'first_name':  'Michael', 'last_name' : 'Jordan'},
    #      {'first_name' : 'John', 'last_name' : 'Rosales'},
    #      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    #      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    #   ],
    #  'Instructors': [
    #      {'first_name' : 'Michael', 'last_name' : 'Choi'},
    #      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    #   ]
    #  }
# Create a program that prints the following format (including number of characters in each combined name):
    # Students
    # 1 - MICHAEL JORDAN - 13
    # 2 - JOHN ROSALES - 11
    # 3 - MARK GUILLEN - 11
    # 4 - KB TONEL - 7
    # Instructors
    # 1 - MICHAEL CHOI - 11
    # 2 - MARTIN PURYEAR - 13

#   ---------------
# Part 1:
# dictionary
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# f(x) print students
def print_student_info(studentlist):
    # loop through items in students
    for items in studentlist:
        print(items['first_name'], items['last_name'])
print_student_info(students)


#   ---------------
# Part 2:
print('-----')
# dictionary
users = {
    'Students': [
        # key:value pair
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}
# f(x) dictinary
def print_school_info(userdict):
    # loop dictinary
    for item in userdict:
        # print item
        print(item)
        # set variable for counting
        counter = 0
        # loop through people in dictionary
        for person in userdict[item]:
            # increment counter variable
            counter+=1
            # print counter + first + last + length of person's name
            print(counter,person['first_name'].upper(),person['last_name'].upper(),'-',(len(person['first_name']) + len(person['last_na'])))
# call f(x)
print_school_info(users)

# L|5
