# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:27:49 2026

@author: gabri
"""
def inputcaller():
    while True:
        try:
            x = f(float(input('Enter any real number:' )))
            return x
        except ValueError:
            print('Oops you inputed something that\'s not a real number, try again!')

def f(x =0):
    print("You've called f(x) which is defined as x**3 + 8\n")
    x = x
    print(f"You chose x to equal {x}\n")
    
    return x**3 + 8 
def f_compare(x):
    return print("YAY!") if x > 17 else print('Too Small')

def main():
    x = inputcaller()
    print(f'The result of f(x) is {x}')
    f_compare(x)

if __name__ == '__main__':
    main()