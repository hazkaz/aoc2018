# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:03:55 2019

@author: HARIKRISHNAN
"""

from collections import Counter

def subtract(a,b):
    diff=0
    for a,b in zip(a,b):
        if a!=b:
            diff+=1
    return diff

with open('input2.txt') as file:
    lines = file.read().strip().split('\n')
    for i,word in enumerate(lines):
        for j,counterpart in enumerate(lines[i+1:]):
            if(subtract(word,counterpart)<=1):
                print(i,word,"-",j,counterpart)
                print("common parts")
                for a,b in zip(word,counterpart):
                    if(a==b):
                        print(a,end='')