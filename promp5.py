# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:03:52 2026

@author: gabri
"""
import numpy as np


def main():   
    x = np.linspace(0, 2*np.pi, 1000)
    
    for i in range(len(x)):
        #sin = np.sin(x[i])
        #print(f"sin(x) = {sin} vs x = {x[i]}")
        print(f"sin(x) = {np.sin(x[i])} vs x = {x[i]}")


if __name__ == '__main__':
    main()