#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:21:51 2019

@author: denisebaker
"""

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")