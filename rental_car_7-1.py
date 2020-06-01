#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:14:55 2019

@author: denisebaker
"""



rental_car = input('Please enter what type of car you would like: ').lower()

if rental_car.lower() == 'subaru':
    print('Let me see if I have a Subaru.')
    
else:
    print('I am sorry.  That car is not available.')