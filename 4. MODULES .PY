# USING MATH MODULE .

import math

def rhombus_area(d1, d2):
    return 1/2*(d1 * d2) 
print(rhombus_area(9, 10)) 


#USING RANDOM MODULE .

import random

def generate_random_numbers(a,b):
    num_list=[]
    for i in range(a,b):
        num_list.append(random.randrange(a,b))
        i+=1
    print(num_list)
generate_random_numbers(10,30)
