#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:30:30 2019

@author: denisebaker
"""

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

friends = ['jen', 'laura', 'mike', 'phil']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is "
              + favorite_languages[name].title() + "!")
        
coders = ['jen', 'edward', 'luis', 'joey']

for coder in coders:
    if coder in favorite_languages.keys():
        print('Hi ' + coder.title() + '. ' + 'Thank you for your response.')
    else:
        print('Hi ' + coder.title() + '. ' + 'Please take our poll.')