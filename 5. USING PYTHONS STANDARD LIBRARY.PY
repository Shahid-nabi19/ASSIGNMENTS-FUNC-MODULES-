# USING MATH 

import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

print(pythagoras(9,12))


#USING RANDOM 


import random

num= random.randrange(1,50)

user_guess= int(input("Enter ur Guess:"))
if user_guess==num:
    print("Your guess is Right")
else:
    print("Your guess is Wrong")
