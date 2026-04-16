# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:50:25 2026

@author: gabri
"""


class animal:
        def __init__(self,name = None, ArmLenght = None, LegLength = None, EyeNumber = None, Tail = None, Furry = None):
            self.name = name
            self.ArmLenght = ArmLenght
            self.LegLength =  LegLength  
            self.EyeNumber = EyeNumber
            self.Tail = Tail
            self.Fur = Furry

        def print(self):
            print(f"\nThe animal we described is {self.name}\n\nThe following is your discription\nThe lenght of its arms is {self.ArmLenght}\nThe length of its legs is {self.LegLength}\nThe number of eyes is {self.EyeNumber}\nIt has a tail is {self.Tail} for this animel.\nIt has fur is {self.Fur} for this animel")
    
def survey():
    name = str(input('Give a name for your animal:'))
    ArmLenght = float(input('Give a float value for arm lenght:'))
    LegLength = float(input('Give a float value for leg length:'))
    EyeNumber = int(input('Give a Int value for the number of eyes:'))
    Tail = input('It has a tail; True or False? ').strip().lower() == 'true'
    Furry = input('It has fur; True or False? ').strip().lower() == 'true'
    return name, ArmLenght,LegLength, EyeNumber, Tail, Furry
def main():
    
    name, ArmLenght,LegLength, EyeNumber, Tail, Furry = survey()
    
    myanimal = animal(name, ArmLenght,LegLength, EyeNumber, Tail, Furry)
    
    myanimal.print()
    
    
    

if __name__ == '__main__':
    main()