#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:11:51 2019

@author: denisebaker
"""

guest_list = ['Michael', 'Chris', 'Flo', 'Gordon']

    
del guest_list[-1]
print(guest_list)
guest_list.append('Anna Lisa')
print(guest_list)

for person in guest_list:

    print(person +  ', please join us for dinner.')
    
guest_list.pop()
print(guest_list)
