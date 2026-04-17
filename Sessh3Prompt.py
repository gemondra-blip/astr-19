# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:27:49 2026

@author: gabri
"""
import f_function as poop

def inputcaller():
    while True:
        try:
            x = float(input('Enter any real number:' ))
            return x
        except ValueError:
            print('Oops you inputed something that\'s not a real number, try again!')


def f_compare(x):
    return print("YAY!") if x > 17 else print('Too Small')

def main():
    x = inputcaller()
    x = poop.f(x)
    print(f'The result of f(x) is {x}')
    f_compare(x)

if __name__ == '__main__':
    main()