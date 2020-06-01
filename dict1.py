#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:36:14 2019

@author: denisebaker
"""

glossary = {'input': 'user input',
         'print': 'prints to console',
         'function': 'repeatable code',
         'for loop': 'iterator',
         'variable': 'object',
         'sorted': 'prints in order',
         'dictionary': 'key, value pairs',
         'if / else': 'Boolean iterator',
         'class': 'group',
         'while': 'loops til instance is untrue'}

for word, meaning in glossary.items():

    print('\n' + word.title() + ': ' + meaning.title())