#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:26:36 2019

@author: denisebaker
"""

age = "\nPlease tell me how old you are: "
age += "\nEnter 'quit' when you are finished: "
active = True

while active:
    price = input(age)
    
    if price == 'quit':
        break
    price = int(price)
    
    
    if price < 3:
        
        print('\nYour ticket is free.')
        
    elif price <= 12:
        print("")
        print("\n"'Your ticket is $10.')
        
    elif price > 12:
        print('\nYour ticket is $15.')
    

