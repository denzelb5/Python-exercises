#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:30:33 2019

@author: denisebaker
"""

user1 = {
        'first_name': 'laura',
         'last_name': 'downing',
         'age': 45,
         'city': 'chicago'
         }

user2 = {
        'first_name': 'luis',
         'last_name': 'eagle',
         'age': 12,
         'city': 'nashville'
         }

user3 = {
        'first_name': 'luis',
         'last_name': 'eagle',
         'age': 12,
         'city': 'nashville'
         }

people = [user1, user2, user3]

for person in people:
    print(person)