# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:27:12 2023

@author: Admin
"""


def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        print(fibonacci(6))

        