#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:30:19 2019

@author: denisebaker
"""




def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
        
magicians = ['bozo', 'riley', 'mike']
    
show_magicians(magicians)

def make_great():
    
    great_magicians = []
    
    
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() +' the Great!' 
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)

show_magicians(magicians)