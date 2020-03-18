#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/18 15:01
# @Author: guohz-acmr
# @File  : extends.py


class Pet(object):
    def __init__(self, pid, name, ptype):
        self.pid = pid
        self.name = name
        self.ptype = ptype

    def hungry(self):
        print('Your poor {} {} is so hungry!'.format(self.ptype, self.name))

    def act_cute(self):
        print('OMG!!! Your stupid {} {} is sooooo cute!'.format(self.ptype, self.name))

    def sleep(self):
        print('Wew, {} {} is sleeping'.format(self.ptype, self.name))

    def chat(self):
        pass


class Dog(Pet):
    def __init__(self, pid, name):
        super(Dog, self).__init__(pid, name, 'dog')

    def chat(self):
        print('wang wang wang...')


class Cat(Pet):
    def __init__(self, pid, name):
        super(Cat, self).__init__(pid, name, 'cat')

    def chat(self):
        print('miao miao miao...')


huniu = Cat(1, 'Mirana')
huniu.hungry()
huniu.act_cute()
huniu.chat()
xiaohei = Dog(2, 'Little Black')
xiaohei.hungry()
xiaohei.act_cute()
xiaohei.chat()
print(dir(huniu))
