#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/19 10:24
# @Author: guohz-acmr
# @File  : magic_method.py


class Com(object):
    # name = reg = ''
    def __new__(cls, *args, **kwargs):
        print(args)
        return super(Com, cls).__new__(cls)

    def __init__(self, name, reg):
        self.name = name
        self.reg = reg
        print('init:{}'.format(name))

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        # print(item)
        if item in self.__dict__.keys():
            return super(Com, self).__getattr__(item)
        else:
            return 'Com 类中没有{}属性'.format(item)

    def tostring(self):
        print('{} {}'.format(self.name, self.reg))


# print(dir(Com))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', 'tostring']
"""
acmr = Com('acmr', 'fengtai')
acmr.tostring()
acmr.__setattr__('create', '1989')
acmr.tostring()
print(acmr.creat)
# print(Com.__class__)
# print(Com.__name__)
# print(Com.__dict__)
