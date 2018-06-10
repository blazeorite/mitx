#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:02:06 2018

@author: Sujith
"""
s='oiboboblpbpbp'
bob = 0
for x in range(len(s)):
     if s[x:x+3] == 'bob': 
         bob += 1
print(bob)