#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:27:10 2017

@author: neftali
"""
from random import randint

matrix = []

def createMatrix():
    for i in range(1,53):
        for n in range(1,151):
            x = randint(1,6)
            matrix.append(x)
    n = 0 
    y = 150
    while y <= 7800:
        print('<div class="row-matrix">')
        print ('</span><span class="unit">'.join(str(e) for e in matrix[n+1:n+150]))
        print('</div>')
        n += 150
        y += 150
    
            