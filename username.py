#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:18:24 2019

@author: denisebaker
"""

current_user  = ['admin', 'denzelb', 'laurax', 'wuissy', 'joeyd']
new_user = ['denzelb', 'laurax', 'denviol', 'luis', 'joey']

for entry in new_user, current_user:
    if entry == current_user:
        print("Enter a different name")
    else: 
        print('welcome ' + str(entry))
    