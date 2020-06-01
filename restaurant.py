#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:11:13 2019

@author: denisebaker
"""

class Restaurant():
    """Restaurant info."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Restaurant description"""
        
        print('The name of the restaurant is ' + self.restaurant_name.title())
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type.title() + ' food.')
        
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open.')
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """Add given amount to total served"""
        
        self.number_served += additional_served
        
class IceCreamStand(Restaurant):
    """a subclass for an ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes attribute to describe an ice cream stand"""
        
        super().__init__(restaurant_name, cuisine_type= 'ice cream')
        self.flavors = []
        
        
    def show_flavors(self):
        """printout list of flavors available"""
        for flavor in self.flavors:
            print('Flavor available: ' + flavor.title())
        
bakery = Restaurant('frothy monkey', 'coffee')

print(bakery.restaurant_name)
print(bakery.cuisine_type)
        
bakery.describe_restaurant()
bakery.open_restaurant()
print("\n")
chinese = Restaurant('sampan', 'chinese')
chinese.describe_restaurant()
chinese.open_restaurant()

print("\n")

italian = Restaurant('mafiozas', 'italian')

italian.describe_restaurant()
italian.open_restaurant()

restaurant = Restaurant('thai esane', 'thai')
print(restaurant.number_served)
restaurant.set_number_served(259)
restaurant.describe_restaurant()
print('Number served: ' + str(restaurant.number_served))

restaurant.increment_number_served(75)
print('Number served: ' + str(restaurant.number_served))

jenis = IceCreamStand('Jenis', 'ice cream')
jenis.flavors = ['vanilla', 'chocolate', 'strawberry', 'cookies and cream']
print(jenis.flavors)
jenis.show_flavors()








