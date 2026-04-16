# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:47:44 2026

@author: gabri
"""

def floata():
    print("We're adding two float numbers [ex: 2.0 or 5.5]\nWhole numbers are welcomed, letters would make you restart.")
    while True:
        try:
            A = float(input())
            B = float(input())
            sum_val = A + B
            type_sum = type(sum_val)
            return type_sum, sum_val
        except ValueError:
            print('A wrong input was given, try again.')

def inta():
    print("We're finding the difference of two integers [ex: 2,9,0]\nFloat data types are NOT welcomed.")
    while True:
        try:
            A = int(input())
            B = int(input())
            sum_val = abs(A - B)
            type_sum = type(sum_val)
            return type_sum, sum_val
        except ValueError:
            print('A wrong input was given, try again.')

def floatint():
    print("We're finding the product of a int & float")
    while True:      
        try:
            A = float(input('Enter a float:'))
            B = int(input("Enter a int:"))
            sum_val = A * B
            type_sum = type(sum_val)
            return type_sum, sum_val
        except ValueError:
            return
    
def main():
    # Float sum
    poop, poop2 = floata()
    poop = str(poop)
    print(f'The sum of the floats is {poop2} and it resulted in a data type {poop[8:-2]}\n')

    # Integer Difference section
    poop3, poop4 = inta()
    poop3 = str(poop3)
    print(f'The difference of the two ints is {poop4} and its resulting data type is {poop3[8:-2]}\n')

    # Float/Int Product section
    poop5, poop6 = floatint()
    poop5 = str(poop5)
    print(f'The product of a float and int is {poop6} and its resulting data type is {poop5[8:-2]}\n')

if __name__ == '__main__':
    main()