# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 2018
@author: lhamon
"""

a=1
b=1

length = int(input('Which Fibonacci Number do you want?  '))

L = []
for i in range(length):
    L.append(i)

for x in L:
    if x == 0:
        L[x] = a
    else:
        L[x] = b
        temp = b
        b = a + b
        a = temp

print(L[length-1])
