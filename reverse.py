#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
 
def reverse_string(name):
    return name[::-1]

def startpy():
    name = "RUTHVIKA"
    reverse_name = reverse_string(name)

    print(reverse_name)

if __name__ == '__main__':
    startpy()