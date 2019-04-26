#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
a = set("lady")
b = set("what")
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)
'''

dic = {'w':116, 'gg':1201, 'lady':401}
del dic['lady']
dic['qq'] = 505
print(type(dic), sorted(dic.keys()), dic.values(), dic['gg'])
'''
dic2 = dict([('a', 1), ('b', 2), ('c', 3)])
print(dic2)
print(id(dic))

word = "hello""a" " world".strip()
print(word)
'''