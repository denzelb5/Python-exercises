#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:24:40 2019

@author: denisebaker
"""

class Restaurant():
    """restaurant messages"""
    
    def __init__(self, name, cuisine_type):
        
        self.name = name
        self.cuisine_type = cuisine_type
    def  describe_restaurant(self):
        msg = self.name.title() + ' serves wonderful ' + self.cuisine_type.title() + '.'
        print('\n' + msg)
        
    def open_restaurant(self):
        msg = "The restaurant is now open."
        print('\n' + msg)
        
jenis = Restaurant('Jenis', 'Ice Cream')
print(jenis.name)
print(jenis.cuisine_type)
jenis.describe_restaurant()
jenis.open_restaurant()