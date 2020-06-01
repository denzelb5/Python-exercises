#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:00:43 2019

@author: denisebaker
"""

def display_message():
    print('\nI am learning about functions.')
    
display_message()


def favorite_book(title):
    
    print('One of my favorite books is ' + title)
    
favorite_book('Alice in Wonderland')


def make_shirt(size= 'large', message= 'I love Python'):
    print(size.title() + ' shirt with the message: ' + message.title())
    
make_shirt('medium', 'game of thrones')

def describe_city(name, country= 'united states'):
    print(name.title() + ' is in ' + country + ' .')
    
describe_city('new york')
describe_city('atlanta')
describe_city('zurich', country= 'switzerland')
    

def city_country(city, country):
    print(city + ' ' + country)
    
    
city_country('milan', 'italy')

def make_album(artist,title, number_of_tracks= ''):
    """A function containing info about a music album"""
    
    album_dict = {'artist': artist.title(), 'album': title.title()}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album_dict

prompt1 = 'Enter your favorite musician: '
prompt2 = 'Enter your favorite album: '

print("Enter 'q' at any time to quit.")

while True:
    
    artist =  input(prompt1)
    if artist == 'q':
        break
    
    
    title = input(prompt2)
    if title == 'q':
        break
    
    
    album = make_album(artist, title)
    print(album)
    
