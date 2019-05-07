#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import os
from collections.abc import Iterable, Iterator

'''
numbers = [1,2,3,4,5]
it = iter(numbers)
for number in it:
    print(number, end=" ")
'''

L = list(range(100))
print(L[0:10:2])
print(L[-10:-1:2])

def trim(s) :
    if len(s) == 0:
        return s
    elif s[0] == " ":
        return trim(s[1:])
    elif s[-1] == " ":
        return trim(s[:-1])
    else :
        return s

print(trim("  a  bc   "))

def findMinAndMax(L) :
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        max, min = 0, 0
        for i in L:
            if not isinstance(i, (int, float)):
                raise TypeError("L you fei shuzi ")
        if L[0] > L[1]:
            max = L[0]
            min = L[1]
        else:
            max = L[1]
            min = L[0]
        for i in L:
            if i > max :
                max = i
            elif i < min:
                min = i
        return (max, min)
print(findMinAndMax([6.1,1,-3,5,5.8]))

print([dir for dir in os.listdir(".")])

def triangles() :
    L = [1]
    while(True) :
        yield L
        L = [1] + [x + y for x,y in zip(L[:-1], L[1:])] + [1]

for n in triangles() :
    if len(n) < 11:
        print(n)
    else:
        break

print(isinstance([], Iterator))