#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import os
from collections.abc import Iterator

'''
numbers = [1,2,3,4,5]
it = iter(numbers)
for number in it:
    print(number, end=" ")
'''

my_list = list(range(100))
print(my_list[0:10:2])
print(my_list[-10:-1:2])


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == " ":
        return trim(s[1:])
    elif s[-1] == " ":
        return trim(s[:-1])
    else:
        return s


print(trim("  a  bc   "))


def find_min_max(arg_list):
    if len(arg_list) == 0:
        return None, None
    elif len(arg_list) == 1:
        return arg_list[0], arg_list[0]
    else:
        for i in arg_list:
            if not isinstance(i, (int, float)):
                raise TypeError("列表中存在非数字类型")
        if arg_list[0] > arg_list[1]:
            maximum = arg_list[0]
            minimum = arg_list[1]
        else:
            maximum = arg_list[1]
            minimum = arg_list[0]
        for i in arg_list:
            if i > maximum:
                maximum = i
            elif i < minimum:
                minimum = i
        return maximum, minimum


print(find_min_max([6.1, 1, -3, 5, 5.8]))
print([direction for direction in os.listdir(".")])
print('\n'.join(['  '.join(['%d * %d =  %d' % (a, b, a * b) for a in range(1, b + 1)]) for b in range(1, 10)]))


def triangles(length):
    arg_list = [1]
    rows = 0
    while rows < length:
        yield arg_list
        arg_list = [1] + [m + n for m, n in zip(arg_list[:-1], arg_list[1:])] + [1]
        rows += 1


for row in triangles(10):
    print(row)

# draw_triangles(5)
print(isinstance([1, 2, 3], Iterator))


def fabo(num):
    a = b = 1
    for i in range(num):
        yield a
        a, b = b, a + b


for x in fabo(100):
    print(x)
print(' '.join(['{}'.format(num) for num in reversed(my_list)]))
print(dict(zip(['uid', 'name', 'age'], [1, 'guoguo', 30])))
