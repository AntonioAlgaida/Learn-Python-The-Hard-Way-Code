# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:43:56 2018

@author: Antonio
"""

#%%
# =============================================================================
# Exercise 13 - Parameters, Unpacking, Variables
# =============================================================================

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)