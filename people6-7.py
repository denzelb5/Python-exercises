#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:04:42 2019

@author: denisebaker
"""

pet1 = {
        'variety': 'dog',
        'name': 'bailey',
        'color': 'black',
        'age': 13,
        'weight': 55
        }

pet2 = {
        'variety': 'dog',
        'name': 'mikey',
        'color': 'black',
        'age': 3,
        'weight': 70
        }

pet3 = {
        'variety': 'dog',
        'name': 'lady',
        'color': 'brown',
        'age': 8,
        'weight': 60
        }

pets = [pet1, pet2, pet3]

for pet in pets:
    print(pet)