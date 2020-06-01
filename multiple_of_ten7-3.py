#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:21:03 2019

@author: denisebaker
"""

number = input('Please enter a number: ')
number = int(number)

if number % 10 == 0:
    print('This is a multiple of 10.')
else:
    print('This is not a multiple of 10.')