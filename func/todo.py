#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/16 17:41
# @Author: guohz-acmr
# @File  : todo.py
"""
    Test the functions in function.py
"""

from func.function import *

print(__name__)
print(selfdef_sum(1, '1'))
print(division(3, 2))
print(division(3, 0))
print(2 / 1)
print(9 // 5)
print(division(1, 2))
print(division(-3, 2))
show_user(1, 'guoguo', sex='male', age=('1', '2', '3'))
lsum = lambda num1, num2: num1 + num2
print(lsum(1, 1))
