#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/20 13:35
# @Author: guohz-acmr
# @File  : descriptors.py


class Desc(object):
    def __init__(self, name):
        print('desc init: {}'.format(self))
        self.name = name

    def __get__(self, instance, owner):
        if not isinstance(self.name, str):
            print('err:{} is not integer'.format(self.name))
            return -1
        print('desc get:{}--{}--{}'.format(self, instance.__dict__, owner))
        return self.name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            print('err:{} is not integer'.format(value))
            return -1
        print('desc set:{}--{}--{}'.format(self, instance, value))
        self.name = value


class Owner(object):
    desc = Desc('name')

    def __init__(self, myname):
        print('owner init: {}'.format(self))
        self.desc = myname


owr = Owner('guoguo')
owr.desc = 'qian'
print(owr.desc)
