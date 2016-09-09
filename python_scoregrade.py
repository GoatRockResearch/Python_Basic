#   Python Exercise: Scores & Grades

# Python Import Modules:
from __future__ import print_function

# Instructions:
# 1. Create a program that prompts the user ten times for a test score between 60 and 100;
# 2. Each time a score is generated display grade of that score;
# 3. Here is the grade table:
#    Score: 60 - 69; Grade - D
#    Score: 70 - 79; Grade - C
#    Score: 80 - 89; Grade - B
#    Score: 90 - 100; Grade - A
# 4. Output:
#    Scores and Grades:
#    Score: 87; Your grade is B
#    Score: 67; Your grade is D
#    Score: 95; Your grade is A
#    Score: 100; Your grade is A
#    Score: 75; Your grade is C
#    Score: 90; Your grade is A
#    Score: 89; Your grade is B
#    Score: 72; Your grade is C
#    Score: 60; Your grade is D
#    Score: 98; Your grade is A
#    End of the program. Bye!

# Knowns:
# Collect 10 scores from the user; need collection = list
# Score must be between 60 - 100;
# Submitted score must return grad of that score;

# Unknowns:
# User input: objective is to deal with this;


# Method 1:
print('Method 1:')

# Scores list
scores = []
# f(x) to check score entered fits parameters given to user
def printGrades(grades):
    for grade in grades:
        if grade < 70:
            print('Score: {}; Your grade is a D.' .format(grade))
        elif grade < 80:
            print('Score: {}; Your grade is a C.' .format(grade))
        elif grade < 90:
            print('Score: {}; Your grade is a B.' .format(grade))
        else:
            print('Score: {}; Your grade is an A.' .format(grade))

    # Check Length of grades list
    print('=====')
    print('# of Scores Entered:',len(scores))
# f(x) to collect user input and check if input is int
def getScores():
    while (len(scores) < 10):
        try:
            userinput = int(
                raw_input('Enter a score between 60 and 100 ten times: ')
            )
        # Check for int
        except ValueError:
            print('Enter a whole number only.')
        # Check for score in range
        else:
            if not 60 < userinput <= 100:
                print('Enter a whole number score between 60 and 100')
            # If score meets parameters above, append to scores variable
            else:
                scores.append(userinput)
                print('-----')
                print('Score Added.')
                print('-----')
    # Print Grades
    print('=====')
    print('Scores and Grades')
    print('=====')
    printGrades(scores)
    print('=====')
    print('End of the program. Bye.')
# Call f(x)
getScores()

# L|5
