# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:43:36 2023

@author: Admin
"""

# print positive numbers in a list 
# input of list
li=[]
n=int(input("enter size of list"))
for i in range (0,n):
    e=int(input("enter element of list"))
    li.append(e)
     
    print("positive numbers in ",li,"are:" )
    
    # using lambda function
    pos_num = list(filter(lambda x: (x>=0),li))
    print(pos_num)

