# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 00:00:44 2023

@author: Admin
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('mississippi'))


