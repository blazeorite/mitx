#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:27:20 2018

@author: Sujith
"""

s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print( "Longest substring in alphabetical order is:", longest)
