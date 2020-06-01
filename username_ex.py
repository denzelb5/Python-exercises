#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:03:59 2019

@author: denisebaker
"""

username  = [input('Enter your username: ')]

if username:
    for user in username:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user) 
            
else: 
    print('We need to find some users!')