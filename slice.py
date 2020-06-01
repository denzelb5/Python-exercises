#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:48:19 2019

@author: denisebaker
"""

pizza = ['ham', 'pepperoni', 'hawaiian', 'cheese']
friend_pizza = pizza[ : ]
print(pizza)
pizza.append('sausage')
friend_pizza.append('mushroom')
print(pizza)
print(friend_pizza)
for item in pizza:
    print('My favorite pizzas are: ' + str(item))
for item in friend_pizza:
    print("My friend's favorite pizzas are: " + str(item))