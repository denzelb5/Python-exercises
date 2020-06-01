#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:35:48 2019

@author: denisebaker
"""

rivers = {'Nile': 'Egypt',
          'Rhine': 'Germany',
          'Moldau': 'Czech Republic'}

for river, country in rivers.items():
    print('The ' + river + ' in ' + country + ' is beautiful!')