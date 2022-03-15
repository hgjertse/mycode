#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'The letter grade for your test score is '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your numeric test score? "))

# if input value was higher or equal to 90
if connection >= 90:
    message = message + 'an A.'
    print("You are a scholar!")
elif connection >= 80:
    message = message + 'a B.'
elif connection >= 70:
    message = message + 'a C.'
elif connection >= 60:
    message = message + "a D"
elif connection > .000000011:
    message = message + "a F"
    print("Study harder next time!")
else:
    message = message + 'a F. You forgot to take the test.'
print(message)

