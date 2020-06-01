#!/usr/bin/env python3
# -*- coding: utf-8 -*
vowels =  ['a', 'e', 'i', 'o', 'u']
sentence = "My dog has fleas"
numVowels = 0
 
for char in sentence:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
    
        print(numVowels)
        