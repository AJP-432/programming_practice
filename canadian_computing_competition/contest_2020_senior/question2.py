# Escape Room
# https://cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf

# Ajlal Paracha Dec 15, 2021

import math

def factorize(val_to_fac):
    """Returns prime factorization as a string"""
    anwser = ""

    # Divides out as many 2's as possible, appending them to the anwser
    while val_to_fac % 2 == 0: 
        anwser += "2 "
        val_to_fac /= 2
    
    # Going through all odd numbers from 3 to root of value 
    for i in range(3, math.ceil(val_to_fac/2), 2):
        # If the odd number divides value, add to anwser
        while val_to_fac % i == 0:
            anwser += (str(i) + " ")
            val_to_fac /= i

    return anwser

def get_out():

    values = []
    number_of_rows = int(input("How many rows: "))
    number_of_columns = int(input("How many columns: ")) 

    for i in range(number_of_rows):
        values.append(input().split(" "))

    for i in range(number_of_rows):
        print(values[i])
        
# get_out()
factorize(30)

    
