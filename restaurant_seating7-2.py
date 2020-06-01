#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:16:48 2019

@author: denisebaker
"""

table = input('Enter the number in your party: ')
table = int(table)

if table > 8:
    print('I am sorry.  You will have to wait for a table.')
    
else:
    print('Your table is ready')