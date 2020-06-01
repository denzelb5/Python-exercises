#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:05:28 2019

@author: denisebaker
"""
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished:  "


while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print('I will add ' + toppings + ' to your pizza.')
        
    else:
        break





