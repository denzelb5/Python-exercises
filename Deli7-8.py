#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:38:07 2019

@author: denisebaker
"""

sandwich_orders = ['club', 'pastrami', 'ham', 'peanut butter', 'chicken','pastrami', 'steak', 'pastrami']

finished_sandwiches = []

print('We apologize but we are out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print("\n")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    
    
   
    print('We are making your ' + current_order + ' sandwich.')
    
    finished_sandwiches.append(current_order)
print("\n")
    
for sandwich in finished_sandwiches:
    print('Your ' + sandwich + ' sandwich is ready.')