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

def divide_name (name):
    return name.split(" ")

def reverse_string(name):
    return name[::-1]

def startpy():
    name = "Raja CSP Raman"
    
    dividedname = divide_name(name)
    print("first name: " + dividedname[0])
    print("Middle name: " + dividedname[1])
    print("Last name: " + dividedname[2])

if __name__ == '__main__':
    startpy()