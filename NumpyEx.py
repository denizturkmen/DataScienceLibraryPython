# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:30:15 2020

@author: turkm
"""


import numpy as np 

array = np.array([1,2,3])
print(array)
print(type(array))
array[0]=5
print(array)
print()

ikiarray = np.array([[2,3,4],[5,6,7]])
print(ikiarray)
print(ikiarray[0,2])
print()

print(np.zeros((3,2)))
print()

print(np.full(((3,2)), 42))
print()

print(np.eye(3))
print()

a_matrix = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a_matrix)
print()

print(a_matrix[1:2,2:])
print(a_matrix[:,3])
print()

print(np.arange(1, 11,1))
print()

a = np.linspace(3,20,30)
print(a)
